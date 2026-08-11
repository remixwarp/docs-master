---
title: 狀態管理
sidebar_position: 5
---

# 狀態管理

編輯器將其界面狀態保存在一個 Redux store 中。本頁列出構成該 store 的實際 reducer，並解釋 action creator、選擇器和中間件如何圍繞它們組織。

## Store 形狀

store 在 `src/lib/components/app-state-hoc.jsx` 中從三個頂層 reducer 創建：

- **`scratchGui`** 是編輯器狀態樹，在 `src/reducers/gui.js` 中構建。
- **`locales`** 持有活動語言和 RTL 標誌（`src/reducers/locales.js`）。
- **`scratchPaint`** 是造型編輯器自己的 store，從 scratch-paint 導入。

編輯器觸及的幾乎所有內容都在 `scratchGui` 下。該切片本身在 `src/reducers/gui.js` 中用 `combineReducers` 組裝，`src/reducers/` 中每個文件對應一個子 reducer。

## Reducers

下面的每個條目都是組合進 `scratchGui` 的真實切片，定義它的文件在 `src/reducers/`。讀取狀態意味著 `state.scratchGui.<slice>`。

**項目生命週期**

- `projectState`（`project-state.js`）跟蹤當前項目的加載、保存和錯誤狀態，並導出 `getIsError` 和 `getIsShowingProject` 等選擇器。
- `projectTitle`（`project-title.js`）是項目名稱。
- `projectChanged`（`project-changed.js`）跟蹤是否有未保存的更改。
- `autosave`（`autosave.js`）持有自動保存狀態。

**運行時和 VM**

- `vm`（`vm.js`）持有唯一的 VM 實例（在這裡創建一次）和任何其他可序列化的東西。
- `vmStatus`（`vm-status.js`）鏡像運行、啟動和渦輪狀態。
- `tw`（`tw.js`）持有 TurboWarp 運行時選項：幀率、插值、編譯器選項、編譯錯誤、雲變量存在性和平臺不匹配詳情。

**目標和監視器**

- `targets`（`targets.js`）是角色和舞臺列表以及正在編輯的目標。
- `hoveredTarget`（`hovered-target.js`）跟蹤拖放的懸停角色。
- `monitors`（`monitors.js`）持有變量和列表監視器，`monitorLayout`（`monitor-layout.js`）跟蹤它們的位置。

**編輯器佈局和標籤頁**

- `mode`（`mode.js`）是佈局的大切片：`isPlayerOnly`、`isFullScreen`、`isEmbedded`。它決定渲染完整編輯器還是隻渲染播放器。
- `editorTab`（`editor-tab.js`）是活動標籤頁（代碼、造型、聲音）。
- `stageSize`（`stage-size.js`）和 `customStageSize`（`custom-stage-size.js`）控制舞臺尺寸。
- `workspaceMetrics`（`workspace-metrics.js`）按目標記住積木工作區的滾動和縮放。
- `toolbox`（`toolbox.js`）持有積木區 XML 狀態。

**模態框、菜單和覆蓋層**

- `modals`（`modals.js`）是哪些模態框打開的地圖（素材庫、設置、git、還原點、字體、資產、調試器等），由 `openModal` / `closeModal` action creator 切換。
- `menus`（`menus.js`）跟蹤哪些菜單欄下拉框打開。
- `cards`（`cards.js`）是教程卡片組，`alerts`（`alerts.js`）是警報隊列，`toast`（`toast.js`）是短暫的 toast 消息。
- `connectionModal`（`connection-modal.js`）是外設連接狀態。
- `colorPicker`（`color-picker.js`）支撐取色器。
- `micIndicator`（`mic-indicator.js`）是麥克風電平指示器。
- `onboarding`（`onboarding.js`）驅動首次運行的引導流程。

**拖動、恢復和歷史**

- `blockDrag`（`block-drag.js`）和 `assetDrag`（`asset-drag.js`）跟蹤進行中的拖動。
- `restoreDeletion`（`restore-deletion.js`）支撐"恢復最後刪除的"操作。
- `timeTravel`（`time-travel.js`）持有積木主題的"年份"，用於重新鍵控積木工作區。

**主題**

- `theme`（`theme.js`）持有當前 `Theme` 對象，並在它更改時應用其顏色。
- `mwProjectTheme`（`mw-project-theme.js`）支撐應用嵌入項目中的主題的提示。請參閱[主題](/internals/theming)。

**RemixWarp 添加和其他**

- `rotur`（`rotur.js`）持有社區集成使用的 Rotur 賬戶和會話狀態。
- `collaboration`（`collaboration.js`）持有實時協作狀態。
- `shortcuts`（`shortcuts.js`）持有鍵盤快捷鍵配置。
- `fontsLoaded`（`fonts-loaded.js`）跟蹤字體加載，`timeout`（`timeout.js`）是一個小型共享超時切片。

## Action creator 和選擇器

每個 reducer 文件遵循相同的約定：它定義其 action 類型常量和 reducer，並默認導出 reducer 加上它的 action creator（有時還有選擇器和它的 `initialState`）。例如 `theme.js` 導出 `setTheme`，`vm.js` 導出 `setVM`，`project-state.js` 在其 actions 旁邊導出 `getIsError` 等選擇器。

容器直接導入這些。`mapStateToProps` 讀取切片（或調用選擇器），`mapDispatchToProps` 包裹一個導入的 action creator，使組件接收普通的回調。模式請參閱[容器](/internals/containers)。

## 初始狀態和渲染模式

`gui.js` 還導出 `guiInitialState` 以及為受限視圖轉換它的輔助工具：`initPlayer`、`initFullScreen` 和 `initEmbedded`。`AppStateHOC` 在創建 store 之前應用這些，因此同樣的 reducer 可以支撐完整編輯器、播放器或嵌入，只在 `mode` 切片上有所不同。

## 中間件

`scratchGui` store 用一箇中間件 `guiMiddleware` 增強，定義在 `gui.js` 中。它是配置為合併快速重複 actions（leading 和 trailing，300 毫秒）的 `redux-throttle`，這防止來自 VM 的高頻更新壓垮 React。`AppStateHOC` 還包裹組合的 reducer 以在每個 action 後通知插件系統（`AddonHooks.appStateReducer`），並在 `window.ReduxStore` 上暴露 store 供調試和插件使用。

## 另請參閱

- [容器](/internals/containers)
- [架構](/internals/architecture)
- [主題](/internals/theming)
- [插件系統](/internals/addons-system)
