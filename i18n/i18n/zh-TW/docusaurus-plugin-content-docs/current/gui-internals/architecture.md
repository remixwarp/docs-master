---
title: 架構
sidebar_position: 2
---

# 架構

RemixWarp 看起來像一個應用，但實際上是構建時組合在一起的一組獨立包。本頁是自頂向下的地圖：各包是什麼、項目如何從工作區中的積木流到舞臺上的像素、它如何保存和加載，以及編輯器、插件、主題引擎和社區層如何圍繞核心排列。本節的後續頁面放大各個部件；從這裡開始看它們如何連接。

## 各包

RemixWarp 是 TurboWarp 的分叉，TurboWarp 是 Scratch 的分叉，它繼承了 Scratch 拆分為獨立 npm 包的佈局。每個包都是自己的倉庫，獨立開發並鏈接到編輯器構建中。

- **scratch-gui** 是編輯器和社區站點：一個由 webpack 打包的 React 加 Redux 應用。它擁有界面、Redux store、主題引擎、插件框架和社區 SPA。您看到的一切都是 scratch-gui；本內部節的幾乎所有內容都是關於它的。
- **scratch-vm** 是引擎。它是純 JavaScript，沒有 React。它擁有運行時、目標（角色和舞臺）、積木、線程、解釋器和 JS 編譯器。它是項目實際做什麼的真相來源。
- **scratch-render** 在 WebGL 畫布上繪製舞臺。VM 擁有一個渲染器實例並告訴它每個角色、造型和畫筆痕跡去哪裡。
- **scratch-blocks** 是 Google Blockly 的一個分叉。它繪製積木工作區和積木區，並將積木編輯變成 VM 應用的更改。
- **scratch-paint** 是造型和背景編輯器（一個繪畫程序）。它有自己的 Redux store，這就是編輯器的 store 有獨立 `scratchPaint` 切片的原因。
- **scratch-audio** 播放和處理聲音：VM 將音頻緩衝區和效果參數交給它。

開發時這些通過 `pnpm run link` symlink 到 scratch-gui 中，因此例如 scratch-vm 的更改無需重新發布就會出現在編輯器中。工作區佈局請參閱[項目結構](/development/project-structure)。

## 各部分如何對話

運行時編輯器恰好持有一個 VM 實例。scratch-gui 自己不運行項目；它驅動 VM 並將界面需要的 VM 狀態部分鏡像到 Redux 中。

```
用戶
 |
 v
scratch-gui (React 組件 + Redux store)
 |            ^
 | 調用       | 事件 -> Redux actions
 v            |
scratch-vm  (Runtime, Targets, Blocks, Sequencer, Compiler/Interpreter)
 |   |   |
 |   |   +--> scratch-audio   (聲音播放)
 |   +------> scratch-render   (WebGL 舞臺)
 +----------> scratch-blocks   (工作區 + 積木區，編輯流回 VM)
```

交互是一個循環。用戶在組件中做一些事；容器要麼分發一個 Redux action，要麼調用 VM 上的方法。VM 做工作併發出事件。`vmListenerHOC` 將這些事件翻譯成 Redux actions，連接的組件重新渲染，界面趕上運行時。因為 VM 是真相來源，Redux 從不嘗試持有整個項目；它持有 UI 讀取的切片的鏡像。

接下來的部分跟隨一個項目穿過這個循環：從工作區進入運行時、輸出到渲染器、回到磁盤。

## 從積木到執行

積木存在於兩個保持同步的地方。在工作區中，**scratch-blocks** 擁有可視積木。在 VM 中，每個目標有一個 `blocks` 容器（`scratch-vm/src/engine/blocks.js`），將相同的腳本存儲為按積木 ID 鍵控的普通數據。當您拖動或編輯積木時，scratch-blocks 觸發一個事件，VM 對其積木容器應用相應的更改，兩個表示保持對齊。RemixWarp 從 VM 的積木對象構建工作區，而不是往返 XML，因此這座橋是真正的耦合點（積木區和影子輸入是惰性構建的）。

運行項目意味著運行線程。當帽子積木觸發時（綠旗、按鍵、廣播），運行時為那個腳本啟動一個**線程**（`engine/thread.js`）。每幀**序列器**（`engine/sequencer.js`）在一個時間預算（`WORK_TIME`，幀的四分之三）的一小部分內步進每個活動線程，然後讓出讓幀渲染。這個"步進一點、渲染、步進一點"的節奏讓腳本看起來並行運行。線程和序列器模型在[線程](/api-reference/threads)下完整記錄。

每個線程以兩種方式之一運行：

- **解釋。** `engine/execute.js` 直接遍歷積木樹，查找每個操作碼的函數並調用它。這是始終可用的路徑，也是腳本第一次被步進的運行方式。
- **編譯。** RemixWarp 的 JS 編譯器（`scratch-vm/src/compiler/`）將腳本變成真正的 JavaScript 函數。`compile.js` 運行中間表示生成器（`irgen.js`）、優化器（`iroptimizer.js`）和 JS 生成器（`jsgen.js`）；生成的函數由 `jsexecute.js` 執行。編譯腳本比解釋腳本快得多。編譯默認開啟（`runtime.compilerOptions.enabled`），可以在設置中關閉，此時一切都回退到解釋器。

兩條路徑產生相同的可見行為；編譯器是同一語義上的速度層。運行時、它的選項以及它如何決定編譯在 [VM API](/api-reference/vm-api) 中介紹。

## 渲染舞臺

運行時不繪製任何東西。每個目標保持它的位置、造型、大小、效果和畫筆狀態，並將它們報告給 **scratch-render**，它在共享的 WebGL 畫布上將每個角色繪製為紋理四邊形。VM 擁有那個畫布；scratch-gui 只定位它並在上面繪製覆蓋層：變量和列表監視器、拖動層、綠旗點擊捕獲器，這些從不接觸 WebGL。當目標移動或切換造型時，VM 告訴渲染器，下一幀反映它。造型和背景編輯是一個單獨的關注點，由**scratch-paint** 在造型和聲音標籤頁處理。

## 保存和加載

項目被序列化為 **sb3** 格式，一個包含 `project.json` 加資產文件（SVG 或 PNG 造型、WAV 或 MP3 聲音）的 ZIP，每個資產按字節的 MD5 哈希命名。

- **序列化。** `scratch-vm/src/serialization/sb3.js` 遍歷運行時、目標、積木、變量和監視器並寫入 `project.json`；資產從每個目標的造型和聲音中收集。編輯器將這些打包成一個 `.sb3`。較舊的 `sb2.js` 處理導入遺留的 Scratch 2 項目。
- **反序列化。** 加載反轉這個過程：解析 `project.json`、重建目標和它們的積木容器，並按哈希加載每個引用的資產。`validate-project.js` 在進入時對 JSON 做健全性檢查。
- **存儲。** 資產是內容尋址的，因此許多角色共享的同一個造型只存儲一次。編輯器的存儲層將資產哈希解析為其字節，無論來自 sb3、後端還是內置素材庫。

字節實際存放在哪裡取決於項目如何打開：本地文件、內置項目獲取器或社區後端。發佈流水線（創建、上傳 sb3 和縮略圖，然後分享）在下面以及[項目管理](/user-guide/project-management)和[打包](/user-guide/packaging)中描述。

## 編輯器外殼

React 側是容器與組件拆分。**組件**（`src/components/`）渲染標記並接受一切作為 props；它們不知道 Redux 存在。**容器**（`src/containers/`）將組件連接到 Redux store 和 VM。這個拆分是 scratch-gui 的支柱，在[組件](/gui-internals/components)和[容器](/gui-internals/containers)中介紹。

界面狀態存在於一個 Redux store 中，在 `src/lib/components/app-state-hoc.jsx` 中從三個頂層 reducer 構建：`scratchGui`（大的編輯器樹，在 `src/reducers/gui.js` 中組裝）、`locales`（語言和 RTL）和 `scratchPaint`（畫板編輯器的 store）。`AppStateHOC` 還為播放器、全屏和嵌入模式播種受限的初始狀態，在每個 action 後通知插件系統，並在 `window.ReduxStore` 上暴露 store。切片的完整列表在[狀態管理](/gui-internals/state)中。

頂層組件在 `src/containers/gui.jsx` 中組合。連接的 `GUI` 被包裹在一堆高階組件中，每個橫切關注點一個，使用 redux 的 `compose` 純粹作為函數組合輔助工具：

```js
const WrappedGui = compose(
    LocalizationHOC,
    ErrorBoundaryHOC('Top Level App'),
    TWThemeManagerHOC,
    TWFullScreenResizerHOC,
    FontLoaderHOC,
    ProjectFetcherHOC,
    SB3PostMessageHOC,
    TitledHOC,
    ProjectSaverHOC,
    vmListenerHOC,
    vmManagerHOC,
    SBFileUploaderHOC,
    cloudManagerHOC
)(ConnectedGUI);
```

每個 HOC 負責一件工作：本地化、崩潰邊界、應用主題（放置較早以便圖標在首次繪製前重新著色）、全屏調整大小、字體加載、獲取和保存項目、從 `postMessage` 和本地文件加載、雲變量，以及兩個 VM 橋接 HOC。VM 橋是 `vmManagerHOC`（驅動 VM：附加音頻、啟動它、加載項目數據）和 `vmListenerHOC`（監聽 VM 事件並分發 Redux actions）。VM 實例本身在 `vm` reducer（`src/reducers/vm.js`）中創建一次，並作為穩定引用保存在 store 中，任何容器都可以通過 `state.scratchGui.vm` 到達它。

渲染的 `GUIComponent`（`src/components/gui/gui.jsx`）佈置菜單欄、代碼/造型/聲音標籤頁、積木工作區、舞臺、目標面板和每個模態框。設置 `isPlayerOnly` 時它只渲染舞臺，這就是播放器和嵌入複用編輯器代碼的方式。面向用戶的導覽請參閱[編輯器界面](/user-guide/interface)和[工作區](/user-guide/workspace)頁面。

## 插件、窗口和主題

兩個編輯器子系統位於 React 樹旁邊而不是內部。

- **插件**（`src/addons/`）是從 Scratch Addons 移植的小型編輯器功能。一個 `SettingsStore` 持有每個插件的啟用標誌和設置，持久化到 `localStorage`；插件訂閱並在設置更改時做出反應。一些插件通過一個共享窗口系統打開浮動面板，該系統渲染頁內窗口，或在桌面應用中渲染真正的操作系統窗口。請參閱[插件系統](/gui-internals/addons-system)。
- **主題**（`src/lib/themes/`）將 `Theme` 對象變成寫在 `document.documentElement` 上的 CSS 自定義屬性，加上提供給 scratch-blocks 的積木顏色。因為屬性是無前綴的（`--ui-primary`、`--text-primary`），任何組件都用 `var(...)` 消費它們，社區站點必須將自己的屬性加 `--mw-*` 前綴以避免衝突。請參閱[主題](/gui-internals/theming)。

## 身份與社區層

RemixWarp 不是僅本地的。scratch-gui 還從同一個 webpack 構建提供社區站點（`src/community/`），編輯器有通往它的鉤子。

身份基於 Rotur（`src/lib/rotur/identity.js` 是兩個應用的唯一真相來源）。用戶用 Rotur 令牌登錄，它被換成一個 7 天的 RemixWarp 會話令牌；兩個應用都訂閱該狀態，退出會清除它。前端在 `https://mwapi.mistium.com/api` 用 Bearer 令牌認證調用後端。Rotur 社交功能（帖子、點贊、關注、頭像）直接轉到 `https://api.rotur.dev`。

發佈項目是先上傳的：編輯器創建項目記錄、上傳 sb3 和縮略圖（服務器解壓它並存儲內容尋址資產），用戶在站點上分享它。設置和主題以最後寫入者獲勝的方式同步到賬戶。這些流程由 `rotur` 和 `collaboration` Redux 切片支撐（請參閱[狀態管理](/gui-internals/state)），並且超出本內部節的範圍，本內部節聚焦於編輯器引擎；在此註明它們以便整個圖景可見。

## 另請參閱

- [組件](/gui-internals/components)
- [容器](/gui-internals/containers)
- [狀態管理](/gui-internals/state)
- [主題](/gui-internals/theming)
- [插件系統](/gui-internals/addons-system)
- [線程](/api-reference/threads) 和 [VM API](/api-reference/vm-api)
- [項目結構](/development/project-structure)
