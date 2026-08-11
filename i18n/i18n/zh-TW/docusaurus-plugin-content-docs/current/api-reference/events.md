---
title: 事件
sidebar_position: 8
---

`VirtualMachine` 擴展 Node 的 `EventEmitter`。編輯器和播放器監聽這些事件以保持 UI 同步，您也可以：

```js
vm.on('PROJECT_CHANGED', () => {
    console.log('the project was edited');
});
```

VM 以相同名稱重新發出運行時的大部分事件，因此您通常監聽 `vm`。少數只在 `vm.runtime` 上觸發；下面已註明。此列表取自 `scratch-vm/src/virtual-machine.js` 和 `scratch-vm/src/engine/runtime.js`。

## 播放與運行

| 事件 | 觸發時 |
| --- | --- |
| `PROJECT_START` | 綠旗被按下。 |
| `PROJECT_RUN_START` | 線程本幀開始運行（從空閒到活動）。 |
| `PROJECT_RUN_STOP` | 所有線程已停止（從活動到空閒）。 |
| `PROJECT_CHANGED` | 項目以影響序列化的方式被編輯。 |
| `PROJECT_LOADED` | 項目完成加載。在 `vm.runtime` 上觸發。 |
| `TURBO_MODE_ON` / `TURBO_MODE_OFF` | 渦輪模式被切換。 |
| `RUNTIME_STARTED` / `RUNTIME_STOPPED` | 運行時的步進循環開始或停止。 |

## 加載進度

| 事件 | 負載 |
| --- | --- |
| `LOAD_PROGRESS` | `{stage, loaded, total}`，其中 `stage` 是 `unzipping`、`parsing`、`checking`、`building`、`installing` 之一。 |
| `ASSET_PROGRESS` | 項目資產下載時的 `(finished, total)`。 |

## 目標、積木和工作區

| 事件 | 負載 |
| --- | --- |
| `targetsUpdate` | `{targetList, editingTarget}`。目標列表更改或選擇更改。 |
| `workspaceUpdate` | 編輯目標的積木，用於重建積木工作區。 |
| `MONITORS_UPDATE` | 當前監視器（舞臺觀察器）狀態。 |
| `BLOCK_DRAG_UPDATE` / `BLOCK_DRAG_END` | 積木正在 GUI 上拖動 / 拖動完成。 |
| `VISUAL_REPORT` | 要在被點擊的報告積木旁邊顯示為氣泡的值。 |
| `SCRIPT_GLOW_ON` / `SCRIPT_GLOW_OFF` | 腳本開始或停止發光。 |
| `BLOCK_GLOW_ON` / `BLOCK_GLOW_OFF` | 單個積木開始或停止發光。 |
| `PROJECT_STOP_ALL`、`STOP_FOR_TARGET` | 停止按鈕被點擊 / 一個目標被停止。在 `vm.runtime` 上觸發。 |

## 擴展

| 事件 | 觸發時 |
| --- | --- |
| `EXTENSION_ADDED` | 擴展的積木分類被註冊。負載是分類信息。 |
| `EXTENSION_REMOVED` | 擴展被移除。 |
| `EXTENSIONS_REORDERED` | 擴展順序更改。 |
| `EXTENSION_FIELD_ADDED` | 擴展註冊了一個自定義字段類型。 |
| `BLOCKSINFO_UPDATE` | 擴展的積木被刷新（例如 locale 更改後）。 |
| `PERIPHERAL_LIST_UPDATE`、`USER_PICKED_PERIPHERAL`、`PERIPHERAL_CONNECTED`、`PERIPHERAL_DISCONNECTED`、`PERIPHERAL_REQUEST_ERROR`、`PERIPHERAL_CONNECTION_LOST_ERROR`、`PERIPHERAL_SCAN_TIMEOUT` | 外設掃描和連接生命週期。 |

## 設置已更改

這些在匹配的設置器運行後觸發，因此 UI 可以更新：

| 事件 | 負載 |
| --- | --- |
| `RUNTIME_OPTIONS_CHANGED` | 當前的運行時選項。 |
| `COMPILER_OPTIONS_CHANGED` | 當前的編譯器選項。 |
| `FRAMERATE_CHANGED` | 新的幀率。 |
| `INTERPOLATION_CHANGED` | 插值是否開啟。 |
| `STAGE_SIZE_CHANGED` | `(width, height)`。 |
| `COMPILE_ERROR` | 腳本編譯失敗時的 `(target, error)`。 |
| `HAS_CLOUD_DATA_UPDATE` | 項目是否使用雲變量。 |
| `MIC_LISTENING` | 麥克風是否活動。 |
| `LOCALE_CHANGED` | `setLocale` 之後的新 locale。 |

## 積木詢問宿主

一些積木需要宿主 UI 響應。這些在 `vm.runtime` 上觸發：

- `SAY`：角色說話或思考（`say`/`think` 積木）。
- `QUESTION`：一個"詢問並等待"積木正在等待輸入。宿主收集答案並在運行時上發出 `ANSWER` 事件以解除腳本阻塞。

## 另請參閱

- [VM API](/api-reference/vm-api)
- [線程](/api-reference/threads)
- [積木註冊](/api-reference/block-registration)
