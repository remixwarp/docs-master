---
title: 線程
sidebar_position: 6
---

項目是一組腳本，每個運行中的腳本是一個線程。運行時每幀對每個線程步進一點；正是這種步進讓積木運行。本頁描述 `scratch-vm/src/engine/` 中的 `Thread` 和 `Sequencer` 模型。RemixWarp 也可以將腳本編譯為 JavaScript，這改變線程的運行方式，但不改變周圍的模型。

## 線程是什麼

`Thread`（`engine/thread.js`）是一個運行中的腳本。它重要的字段：

- `topBlock`：腳本頂部（帽子或第一個）積木的 ID。
- `target`：運行腳本的角色或舞臺。
- `blockContainer`：線程從中執行的 `Blocks` 容器。通常是目標自己的積木，但積木區中點擊的腳本從 `runtime.flyoutBlocks` 執行。編譯器也讀取它，因此空容器會跳過編譯。
- `stack`：從頂部積木到當前執行積木的積木 ID。進入 C 積木（循環或 `如果`）會壓入此棧；完成時彈出。
- `stackFrames`：每個棧級別一個 `_StackFrame`，持有每級別的執行狀態（`warpMode`、`isLoop`、`justReported`、`waitingReporter`、過程 `params` 以及積木方法可以在讓出期間使用的暫存 `executionContext`）。幀通過空閒列表池化和回收。
- `status`：線程的狀態（見下文）。
- `requestScriptGlowInFrame` / `blockGlowInFrame`：腳本本幀是否應發光以及發光哪個積木 ID。運行時在發出發光事件時讀取這些（見下文）。
- `warpTimer`：線程進入 warp 模式時創建的 `Timer`；請參閱[Warp 模式](#warp-mode)。
- `isKilled`：線程在中間被停止時設置，因此恢復的積木不會越過終點。
- `isCompiled`、`generator`、`procedures`：線程被編譯為 JavaScript 時設置。

每個線程從其目標和頂部積木獲得一個穩定 ID，`target.id & topBlock`（`Thread.getIdFromTargetAndBlock`）。

### 線程狀態

`status` 是五個常量之一：

| 常量 | 值 | 含義 |
| --- | --- | --- |
| `Thread.STATUS_RUNNING` | 0 | 正常執行；逐積木步進。 |
| `Thread.STATUS_PROMISE_WAIT` | 1 | 等待異步積木的 promise。 |
| `Thread.STATUS_YIELD` | 2 | 已讓出；下一步恢復。 |
| `Thread.STATUS_YIELD_TICK` | 3 | 為單個 tick 讓出；恢復時清除。 |
| `Thread.STATUS_DONE` | 4 | 已完成；沒有剩餘積木。 |

### 棧

`Thread` 暴露解釋器和 C 積木實現使用的棧輔助工具：`pushStack(blockId)`、`popStack()`、`peekStack()`、`peekStackFrame()`、`goToNextBlock()`、`reuseStackForNextBlock(blockId)`、`stopThisScript()`，以及過程參數輔助工具 `pushParam`、`getParam`、`initParams`。

## 序列器 {#the-sequencer}

`Sequencer`（`engine/sequencer.js`）運行線程。每幀運行時調用一次 `stepThreads()`，它：

1. 設置工作預算：`WORK_TIME = 0.75 * runtime.currentStepTime`（幀間隔的 75%）。
2. 遍歷 `runtime.threads`，對每個運行中或已讓出的線程調用 `stepThread(thread)`。
3. 只要有活動線程、工作預算未用完，並且要麼渦輪模式開啟要麼沒有積木請求屏幕重繪，就繼續循環。
4. 移除已完成的線程並返回它們。

`stepThread(thread)` 運行一個線程。如果線程已編譯，它交給編譯執行器；否則它從當前積木開始走解釋器，處理報告積木、C 積木分支、promise 和讓出。當積木請求重繪（或預算用完）時，序列器為本幀停止，並在下一幀從停下的地方繼續。

### Warp 模式 {#warp-mode}

Warp 模式（"運行時不刷新屏幕"，也是自定義積木 warp 的基礎）讓一個部分完整運行到完成，不對重繪讓出。warp 線程使用線程自己的 `warpTimer` 對照 `Sequencer.WARP_TIME`（500 毫秒）計時，而不是共享的 `WORK_TIME` 預算，因此失控的 warp 循環不能永遠凍結頁面。

## 啟動線程

線程由運行時創建，而不是大多數代碼直接創建。點擊綠旗調用 `vm.greenFlag()`，它啟動每個綠旗帽子。觸發帽子（廣播、按鍵、擴展 `EVENT` 積木）通過 `runtime.startHats(opcode, optMatchFields, optTarget)`，它找到每個匹配的腳本，尊重帽子的 `restartExistingThreads` 元數據，並返回新線程。在編輯器中點擊腳本調用 `runtime.toggleScript`，並啟動一個保持在線程映射之外的臨時"堆棧點擊"線程。線程啟動、停止和發光時，運行時發出 `*_GLOW_*`、`PROJECT_RUN_START` 和 `PROJECT_RUN_STOP` [事件](/api-reference/events)。要自己啟動線程或監視現有的線程，請參閱[運行時 API](/api-reference/runtime)。

## 編譯線程 {#compiled-threads}

RemixWarp 的編譯器將腳本變成 JavaScript 生成器函數。線程編譯時，`isCompiled` 變為真，步進的是它的 `generator`，而不是解釋器走積木。上面的線程模型（狀態、warp、啟動和停止）不變；只有逐積木執行更快。編譯器默認開啟，可以從[項目設置](/advanced/disable-compiler)關閉。

## 另請參閱

- [運行時 API](/api-reference/runtime) 瞭解啟動線程、目標和 IO 設備
- [積木註冊](/api-reference/block-registration)
- [VM API](/api-reference/vm-api)
- [內部：架構](/internals/architecture)
- [編譯擴展](/building-extensions/compiled/overview)
- [防卡死計時器](/advanced/warp-timer)和[移除限制](/advanced/remove-limits)
