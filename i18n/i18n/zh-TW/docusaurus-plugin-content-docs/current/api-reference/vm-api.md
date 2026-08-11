---
title: VM API
sidebar_position: 2
---

`VirtualMachine` 是運行項目的引擎。它加載和保存項目、控制播放、管理角色/造型/聲音，並持有實際執行積木的 [`Runtime`](/api-reference/threads)。編輯器或播放器打開時，實時實例位於 `window.vm`（請參閱[概覽](/api-reference/overview)）。

該類位於 `scratch-vm/src/virtual-machine.js`，是 `scratch-vm` 包的默認導出：

```js
import VirtualMachine from 'scratch-vm';
const vm = new VirtualMachine();
vm.start();
```

`VirtualMachine` 擴展 Node 的 `EventEmitter`，因此您用 `vm.on(name, handler)` 監聽。它發出什麼請參閱[事件](/api-reference/events)。

## 生命週期

- `start()`：開始運行時的步進循環。在做任何其他事情之前調用一次。
- `quit()`：關閉運行時並釋放句柄。用於測試收尾；之後不要再使用運行時。`stop()` 是已棄用的別名。
- `greenFlag()`：啟動所有綠旗腳本，就像點擊了旗幟一樣。
- `stopAll()`：停止每個運行中的線程和活動（停止符號按鈕）。
- `clear()`：處理當前項目的數據並重置為空運行時。

## 加載項目

- `loadProject(input)` 返回一個 `Promise`。`input` 可以是 JSON 字符串、普通項目對象，或包含 `.sb`、`.sb2` 或 `.sb3` 文件的 `ArrayBuffer`/類型化數組。VM 驗證輸入、反序列化它、加載它需要的任何擴展並安裝目標。Scratch 1（`.sb`）文件會自動轉換。
- `downloadProjectId(id)`：通過附加的存儲模塊按 ID 獲取項目並加載它。需要附加存儲（見下文）。
- `fromJSON(json)`：`loadProject` 的已棄用包裝；請改用 `loadProject`。

```js
const buffer = await fetch('project.sb3').then(r => r.arrayBuffer());
await vm.loadProject(buffer);
vm.greenFlag();
```

## 保存和導出

- `saveProjectSb3(type, options)`：為壓縮的 `.sb3` 返回一個 `Promise`。`type` 是任何 JSZip 輸出類型（默認 `'blob'`）。`options.allowOptimization`（默認 `true`）控制積木/註釋 ID 優化。
- `saveProjectSb3Stream(type, options)`：為相同數據返回一個 JSZip `StreamHelper`，用於流式傳輸大型項目。
- `saveProjectSb3DontZip(options)`：返回將文件名映射到原始字節的 `Record<string, Uint8Array>`，跳過 zip 創建。返回的緩衝區是 VM 自己的；不要修改它們（`project.json` 除外，它是新建的）。
- `toJSON(optTargetId, serializationOptions)`：將整個項目（或給定 `optTargetId` 時的單個角色）序列化為 JSON 字符串。
- `exportSprite(targetId, optZipType)`：為一個角色及其資產的 `.sprite3` zip 返回一個 `Promise`。
- `serializeAssets(targetId)`：為項目的資產（或一個目標的）返回 `[{fileName, fileContent}]`。
- `assets`（getter）：當前運行時中每個資產對象的數組。

## 目標、角色和編輯目標

"編輯目標"是編輯器中當前選中的角色或舞臺。工作區的積木編輯路由到它。

- `editingTarget`：當前選中的 `Target`（一個 `RenderedTarget`），或 `null`。
- `setEditingTarget(targetId)`：切換正在編輯的目標。發出 `targetsUpdate` 和 `workspaceUpdate`。
- `addSprite(input)`：從 `.sprite2`/`.sprite3` 數據（字符串、對象或 ArrayBuffer）添加角色。返回一個 `Promise`。
- `renameSprite(targetId, newName)`：重命名角色（名稱自動去重）。
- `deleteSprite(targetId)`：刪除角色及其克隆體。返回一個恢復它的函數。
- `duplicateSprite(targetId)`：返回一個在副本添加後解析的 `Promise`。
- `reorderTarget(targetIndex, newIndex)`：在列表中移動目標。返回它是否更改。
- `postSpriteInfo(data)`：更新編輯/拖動目標的信息（`x`、`y`、`direction`、`size`、`visible`、`rotationStyle`）。
- `startDrag(targetId)` / `stopDrag(targetId)`：讓目標進入或退出拖動狀態，使積木停止或恢復影響它的位置。
- `setVariableValue(targetId, variableId, value)` / `getVariableValue(targetId, variableId)`：按 ID 寫入或讀取變量。`setVariableValue` 返回它是否成功；`getVariableValue` 返回值或 `null`。

## 造型、聲音和背景

這些作用於編輯目標，除非傳入了目標 ID。大多數返回一個 `Promise`。

- `addCostume(md5ext, costumeObject, optTargetId, optVersion)`、`addCostumeFromLibrary(md5ext, costumeObject)`、`duplicateCostume(costumeIndex)`、`renameCostume(costumeIndex, newName)`、`deleteCostume(costumeIndex)`（返回恢復函數或 `null`）。
- `updateBitmap(costumeIndex, bitmap, rotationCenterX, rotationCenterY, bitmapResolution)` 和 `updateSvg(costumeIndex, svg, rotationCenterX, rotationCenterY)`：替換造型的圖像。
- `getCostume(costumeIndex)`：造型的 SVG 字符串，或 PNG/JPG 的數據 URI。
- `getExportedCostume(costumeObject)` / `getExportedCostumeBase64(costumeObject)`：用於將造型保存到磁盤的原始字節 / base64。
- `addSound(soundObject, optTargetId)`、`duplicateSound(soundIndex)`、`renameSound(soundIndex, newName)`、`deleteSound(soundIndex)`（返回恢復函數或 `null`）。
- `getSoundBuffer(soundIndex)` / `updateSoundBuffer(soundIndex, newBuffer, soundEncoding)`：讀取或替換聲音的解碼音頻。
- `addBackdrop(md5ext, backdropObject)`：向舞臺添加背景。
- `reorderCostume(targetId, costumeIndex, newIndex)` / `reorderSound(targetId, soundIndex, newIndex)`：重新排序；每個返回它是否成功。

## 播放模式和運行時選項

- `setTurboMode(on)`：渦輪模式（循環不對重繪讓出）。
- `setCompatibilityMode(on)`：30 TPS "2.0" 時序。
- `setFramerate(fps)`：目標幀率。RemixWarp 允許任意值。
- `setInterpolation(enabled)`：幀插值，平滑項目原生幀率之上的運動。
- `setStageSize(width, height)`：自定義舞臺尺寸。
- `setRuntimeOptions(options)` / `setCompilerOptions(options)`：切換運行時行為（圍欄、克隆/列表限制、雜項限制）和編譯器行為（啟用/禁用編譯器、防卡死計時器）。每個合併到當前選項中併發出 `*_CHANGED` 事件。
- `setInEditor(inEditor)`、`convertToPackagedRuntime()`：編輯器和打包器用它告訴運行時它處於哪種環境。
- `enableDebug()` / `disableDebug()`：切換調試器的額外檢測。

## 附加子系統

VM 不創建自己的渲染器、音頻引擎或存儲；宿主附加它們。

- `attachRenderer(renderer)` 和 `renderer` getter（返回附加的 `RenderWebGL` 或 `undefined`）。
- `attachAudioEngine(audioEngine)`。
- `attachStorage(storage)`：一個 `scratch-storage` 實例，`downloadProjectId` 和加載素材庫資產需要它。
- `attachV2BitmapAdapter(adapter)`：將 Scratch 2 位圖轉換為 Scratch 3 位圖。
- `setCloudProvider(provider)` / `setVideoProvider(provider)`：接入雲變量和攝像頭後端。
- `postIOData(device, data)`：將輸入送入虛擬 I/O 設備（`keyboard`、`mouse`、`mouseWheel`、`userData` 等）。
- `setLocale(locale, messages)`：更改 VM 的語言；返回一個在積木刷新後解析的 `Promise`。

## 擴展和外設

- `extensionManager`：`ExtensionManager`。用它加載內置和自定義擴展。
- `securityManager`：決定非沙箱擴展可以做什麼的安全管理器。
- `scanForPeripheral(extensionId)`、`connectPeripheral(extensionId, peripheralId)`、`disconnectPeripheral(extensionId)`、`getPeripheralIsConnected(extensionId)`：控制 micro:bit 和 EV3 等擴展的硬件外設。
- `exports`：為擴展作者暴露的內部類，包括 `Sprite`、`RenderedTarget`、`Variable`、`JSZip`，以及用於註冊編譯積木描述符的 `exports.compiler.register(...)`。名為 `these_broke_before_and_will_break_again` 和 `i_will_not_ask_for_help_when_these_break` 的函數觸及不穩定的編譯器內部；名字就是警告。

## 高級：加載實際如何運行

`loadProject` 驗證輸入，然後調用 `deserializeProject`，它清空運行時並按 `projectVersion` 選擇 `sb2` 或 `sb3` 反序列化。結果（目標加上它們使用的擴展集）進入 `installTargets`，它等待異步擴展、通過 `extensionManager` 和 `securityManager` 加載所需擴展、將每個目標添加到運行時、按 `layerOrder` 排序執行順序、選擇一個編輯目標，併發出 `targetsUpdate` 和 `workspaceUpdate`。加載進度通過 `LOAD_PROGRESS` 事件報告，階段為 `unzipping`、`parsing`、`checking`、`building` 和 `installing`。

## 另請參閱

- [事件](/api-reference/events) 瞭解完整的事件列表
- [線程](/api-reference/threads) 瞭解運行時和序列器
- [擴展 API](/api-reference/extension-api) 用於編寫擴展
- [嵌入](/advanced/embedding) 和[打包器](/packager/overview) 用於分發項目
