---
title: 運行時 API
sidebar_position: 5.5
---

`Runtime`（`scratch-vm/src/engine/runtime.js`）是實際運行項目的引擎。[`VirtualMachine`](/api-reference/vm-api) 擁有一個並將其暴露為 `vm.runtime`；擴展以 `Scratch.vm.runtime` 獲得它。它持有每個目標、步進[線程](/api-reference/threads)、通過 IO 設備路由輸入，併發出編輯器監聽的[事件](/api-reference/events)。

`Runtime` 擴展 Node 的 `EventEmitter`，因此 `runtime.on(name, handler)` 和 `runtime.emit(...)` 直接工作。VM 以相同名稱重新發出大多數運行時事件，因此 UI 代碼通常監聽 `vm`；想要原始流的擴展和內部代碼監聽 `runtime`。

本頁涵蓋擴展或 `window.vm` 控制台可以安全觸及的運行時表面。任何以 `_` 前綴的內容都是內部的，不在此涵蓋。

## 目標

"目標"是一個角色或舞臺（一個 `RenderedTarget`）。運行時按執行順序保留它們。

- `runtime.targets`：所有目標的數組，包括克隆，按圖層/執行順序。
- `runtime.getTargetForStage()`：舞臺目標，如果沒有則為 `undefined`。
- `runtime.getSpriteTargetByName(name)`：具有該名稱的第一個原始（非克隆）角色。
- `runtime.getTargetById(id)`：按 ID 的目標（使用內部緩存）。
- `runtime.getTargetByDrawableId(drawableID)`：擁有給定渲染器可繪製對象的目標。
- `runtime.getEditingTarget()`：編輯器中當前選中的目標，或 `undefined`。

```js
// 在編輯器控制台中：
window.vm.runtime.getTargetForStage();
window.vm.runtime.getSpriteTargetByName('Sprite1');
```

## 克隆

- `runtime.clonesAvailable()`：是否還可以創建另一個克隆（計數達到 `runtimeOptions.maxClones` 後為 `false`）。
- `runtime.changeCloneCounter(delta)`：調整實時克隆計數。克隆/刪除積木會調用這個；您很少需要直接使用。

克隆是 `runtime.targets` 中的普通目標；`stopAll()` 處理掉每個非原始克隆。

## IO 設備

`runtime.ioDevices` 分組虛擬輸入設備。積木讀取它們；宿主通過 [`vm.postIOData(device, data)`](/api-reference/vm-api) 供給它們。

| 設備 | 源碼 | 值得注意的讀取 |
| --- | --- | --- |
| `keyboard` | `io/keyboard.js` | `getKeyIsDown(key)` |
| `mouse` | `io/mouse.js` | `getScratchX()`、`getScratchY()`、`getIsDown()`、`getButtonIsDown(button)` |
| `mouseWheel` | `io/mouse-wheel.js` | 滾動增量 |
| `clock` | `io/clock.js` | `projectTimer()`、`resetProjectTimer()` |
| `cloud` | `io/cloud.js` | 雲變量請求 |
| `userData` | `io/user_data.js` | `getUsername()` |
| `video` | `io/video.js` | 用於視頻偵測擴展的攝像頭幀 |

## 項目計時器

Scratch 的 `計時器` 積木讀取 `runtime.ioDevices.clock`：

- `runtime.ioDevices.clock.projectTimer()`：計時器上次重置以來的秒數。
- `runtime.ioDevices.clock.resetProjectTimer()`：將其重置為零。`greenFlag()` 和 `dispose()` 會自動執行此操作。

## 綠旗與停止

- `runtime.greenFlag()`：停止一切，重置項目計時器，觸發 `event_whenflagclicked` 帽子。發出 `PROJECT_START`。這就是 `vm.greenFlag()` 調用的內容。
- `runtime.stopAll()`：停止每個線程，處理掉所有克隆，並清空線程列表。發出 `PROJECT_STOP_ALL`。

## 啟動線程（帽子）

- `runtime.startHats(requestedHatOpcode, optMatchFields, optTarget)`：為每個頂部積木是 `requestedHatOpcode` 帽子的腳本啟動一個線程。`optMatchFields` 按字段值篩選（比較前大寫，因此廣播和按鍵只觸發正確的腳本）；`optTarget` 將其限制為一個目標。返回新線程數組。它尊重帽子的 `restartExistingThreads` 元數據：`true` 重啟匹配的運行中線程，`false` 在已有運行線程時跳過啟動。這就是帶 `HAT`/`EVENT` 積木的擴展讓帽子觸發的方式。請參閱[積木註冊](/api-reference/block-registration)。
- `runtime.allScriptsDo(fn, optTarget)` / `runtime.allScriptsByOpcodeDo(opcode, fn, optTarget)`：迭代每個頂層腳本（可選按頂部積木操作碼篩選）。`startHats` 構建在第二個之上。
- `runtime.toggleScript(topBlockId, opts)`：從其頂部積木啟動（或對於已在運行的點擊，停止）一個腳本，就像在編輯器中點擊它一樣。

這個引擎沒有 `startHatsWithParams` 方法；請通過 `startHats` 的 `optMatchFields` 傳遞字段匹配器。

## 事件

`Runtime` 發出大量事件；擴展和宿主最常用的：

| 事件 | 觸發時 |
| --- | --- |
| `PROJECT_START` | 綠旗被按下。 |
| `PROJECT_STOP_ALL` | 停止按鈕被點擊（或 `stopAll()` 運行）。 |
| `PROJECT_RUN_START` | 本 tick 線程從空閒變為活動。 |
| `PROJECT_RUN_STOP` | 本 tick 最後一個非監視器線程完成。 |
| `PROJECT_LOADED` | 項目完成加載。 |
| `PROJECT_CHANGED` | 項目以影響序列化的方式被編輯。 |
| `TURBO_MODE_ON` / `TURBO_MODE_OFF` | 渦輪模式切換。 |

`PROJECT_RUN_START` / `PROJECT_RUN_STOP` 是圍繞非監視器線程計數的邊緣觸發事件，因此它們在每次空閒/活動轉變時觸發一次，而不是每個線程一次。完整列表請參閱[事件](/api-reference/events)。

## 監視器

監視器是顯示在舞臺上的值觀察器。運行時持有它們的狀態，編輯器從 `MONITORS_UPDATE` 事件渲染它。

- `runtime.requestAddMonitor(monitorRecord)`：添加監視器（如果 ID 存在則就地更新）。
- `runtime.requestUpdateMonitor(delta)`：按 ID 修補現有監視器；返回它是否存在。
- `runtime.requestRemoveMonitor(id)`：移除一個。
- `runtime.requestShowMonitor(id)` / `runtime.requestHideMonitor(id)`：切換可見性；各自返回監視器是否存在。
- `runtime.getMonitorState()`：當前的監視器狀態映射。

## 視覺報告

- `runtime.visualReport(target, blockId, value)`：在點擊的報告積木旁邊顯示值氣泡。只在 `target` 是編輯目標時報告；發出 `VISUAL_REPORT`。當報告積木在工作區中被點擊時，會為您調用。

## 重繪

- `runtime.requestRedraw()`：標記屏幕必須在序列器在本幀運行更多工作之前重繪。更改可見內容的積木會調用這個；一旦請求重繪，序列器就會在本幀停止步進（除非渦輪模式開啟）。請參閱[線程：序列器](/api-reference/threads#the-sequencer)。

## 渦輪和編譯器標誌

這些由引擎讀取，並通過 VM 的設置器設置（它們也發出更改事件）：

- `runtime.turboMode`：循環運行時不對重繪讓出時為 `true`。通過 [`vm.setTurboMode`](/api-reference/vm-api) 設置。
- `runtime.runtimeOptions`：`{maxClones, miscLimits, fencing, caseSensitiveLists, unsafeOptimisations}`。通過 `vm.setRuntimeOptions` 設置。
- `runtime.compilerOptions`：`{enabled, warpTimer}`。通過 `vm.setCompilerOptions` 設置。`enabled` 是 [JavaScript 編譯器](/api-reference/threads#compiled-threads)的開關；`warpTimer` 讓 warp 循環即使在 warp 模式之外也尊重 warp 超時。

## 另請參閱

- [線程](/api-reference/threads) 瞭解這些方法驅動的線程和序列器模型
- [VM API](/api-reference/vm-api) 瞭解支撐上述標誌的公開設置器
- [事件](/api-reference/events) 瞭解完整的事件列表
- [內部：架構](/internals/architecture)
- [構建擴展](/building-extensions/introduction)
