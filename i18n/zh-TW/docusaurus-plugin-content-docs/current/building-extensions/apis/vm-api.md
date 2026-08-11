---
title: VM API
sidebar_position: 3
---

# VM API

VM（虛擬機）運行項目。[非沙箱擴展](/building-extensions/unsandboxed)以 `Scratch.vm` 訪問它，積木函數以 `util.runtime` 訪問它（運行時是 `vm.runtime`）。

```js
if (!Scratch.extensions.unsandboxed) {
  throw new Error('This extension needs the VM');
}
const vm = Scratch.vm;
const runtime = vm.runtime;
```

這些是內部對象，不是凍結的公共 API。保護缺失的值（角色被刪除、擴展卸載），並優先監聽事件而不是輪詢。這些方法中的大多數在 RemixWarp 和 TurboWarp 上都存在；RemixWarp 特有的行為在重要處註明。

## 項目控制

```js
vm.greenFlag();          // 按下綠旗
vm.stopAll();            // 停止所有腳本
vm.setTurboMode(true);   // 渦輪模式開/關
vm.setFramerate(60);     // 目標每秒幀數
vm.setInterpolation(true);
vm.setCompilerOptions({ enabled: true, warpTimer: false });
vm.setRuntimeOptions({ maxClones: 300, miscLimits: true, fencing: true });
vm.setStageSize(width, height);
```

RemixWarp 默認編譯項目（`compilerOptions.enabled` 為 `true`）。幀率和舞臺大小不限於 Scratch 的 30 FPS / 480x360。

## 目標

"目標"是一個角色、克隆體或舞臺。

```js
runtime.targets;                          // 所有目標的數組（舞臺 + 角色 + 克隆）
runtime.getTargetForStage();              // 舞臺目標
runtime.getTargetById(id);                // 按內部 id
runtime.getSpriteTargetByName('Sprite1'); // 按名稱的原始（非克隆）角色
vm.editingTarget;                         // 編輯器中當前打開的角色
```

目標屬性和方法：

```js
const t = runtime.getSpriteTargetByName('Sprite1');
t.x; t.y; t.direction; t.size; t.visible;
t.getName();
t.isStage; t.isOriginal;
t.currentCostume;                         // 索引
t.sprite.costumes[t.currentCostume].name;

t.setXY(100, 50);
t.setDirection(90);
t.setSize(150);
```

### 克隆

```js
const original = runtime.getSpriteTargetByName('Sprite1');
const clone = original.makeClone();
if (clone) {
  runtime.addTarget(clone);
  clone.setXY(100, 50);
}

// 移除克隆（絕不是原始）
if (!clone.isOriginal) runtime.disposeTarget(clone);
```

## 變量和列表

變量和列表位於目標上。變量類型使用 `''`，列表使用 `'list'`。

```js
const stage = runtime.getTargetForStage();

const score = stage.lookupVariableByNameAndType('score', '');
if (score) score.value = 100;

const items = stage.lookupVariableByNameAndType('items', 'list');
if (items) items.value.push('new item');
```

全局變量和列表位於舞臺上；角色局部的位於角色上。要枚舉，請迭代 `target.variables` 並檢查每個條目的 `.type`。

## 啟動腳本

```js
// 啟動每個"當綠旗被點擊"帽子
runtime.startHats('event_whenflagclicked');

// 啟動匹配字段的帽子
runtime.startHats('event_whenbroadcastreceived', { BROADCAST_OPTION: 'message1' });
```

`startHats` 返回啟動的 `Thread` 對象。在運行中的積木內部，請使用 `util.startHats`。請參閱[事件和帽子](/building-extensions/hats)。

## 線程

```js
runtime.threads;              // 運行中的線程
runtime.stopForTarget(target); // 停止目標腳本

thread.target;   // 運行它的目標
thread.topBlock; // 頂部積木的 id
thread.status;   // 見下文
```

線程狀態值：

| 值 | 常量 | 含義 |
|:-:|:--|:--|
| 0 | `STATUS_RUNNING` | 運行中 |
| 1 | `STATUS_PROMISE_WAIT` | 等待 Promise |
| 2 | `STATUS_YIELD` | 本幀已讓出 |
| 3 | `STATUS_YIELD_TICK` | 讓出直到下一個 tick |
| 4 | `STATUS_DONE` | 已完成 |

在積木內部，`util`（積木工具）是您對當前線程的句柄，而不是深入 `runtime.threads`：

- `util.thread` 是運行積木的 `Thread`。
- `util.yield()` 為本幀讓出當前線程（從異步積木返回 Promise 是等待的常規方式；`util.yield()` 是手動等價物）。
- `util.yieldTick()` 讓出直到下一個 tick。
- `util.startBranch(index, isLoop)` 運行 C 積木分支（請參閱[自定義 C 積木](/building-extensions/custom-c-blocks)）。

完整的線程模型、狀態和序列器請參閱[線程參考](/api-reference/threads)。

## 事件

用 `vm.on(...)` 或 `runtime.on(...)` 監聽：

| 事件 | 觸發時 |
|:--|:--|
| `PROJECT_RUN_START` | 腳本開始運行 |
| `PROJECT_RUN_STOP` | 所有腳本已停止 |
| `PROJECT_LOADED` | 項目完成加載 |
| `PROJECT_CHANGED` | 項目被修改 |
| `targetWasCreated` | 創建目標（通常是克隆）；參數 `(newTarget, sourceTarget)` |
| `TARGETS_UPDATE` | 目標列表更改 |
| `BEFORE_EXECUTE` | 每幀，在腳本運行前（對謂詞帽子有用） |
| `MONITORS_UPDATE` | 監視器值更改 |

```js
runtime.on('targetWasCreated', (target) => console.log('created', target.getName()));
vm.on('PROJECT_RUN_START', () => console.log('running'));
```

上表列出了擴展最常觸及的事件。運行時事件的完整集合和生命週期請參閱[運行時參考](/api-reference/runtime)。

## 輸入設備

```js
const mouse = runtime.ioDevices.mouse;
mouse.getClientX(); mouse.getClientY(); mouse.getIsDown();

const keyboard = runtime.ioDevices.keyboard;
keyboard.getKeyIsDown('space');

const clock = runtime.ioDevices.clock;
clock.projectTimer();       // 計時器重置以來的秒數
clock.resetProjectTimer();
```

## 舞臺大小

```js
runtime.stageWidth;   // 當前邏輯寬度
runtime.stageHeight;  // 當前邏輯高度
vm.setStageSize(640, 360);
```

## 擴展管理

```js
const em = vm.extensionManager;
em.isExtensionLoaded('pen');   // 布爾值
em.getExtensionURLs();         // 已加載擴展的 URL
em.refreshBlocks('myextension'); // 更改積木信息後重新渲染積木區
```

## 按項目存儲

`runtime.extensionStorage` 是保存在項目文件內部的對象。以您的擴展 ID 為鍵存儲小的可 JSON 序列化設置：

```js
runtime.extensionStorage.myextension = { volume: 0.5 };
```

## 編譯器內部

要直接生成 JavaScript（原生速度積木），RemixWarp 通過 `vm.exports.compiler` 暴露受支持的擴展編譯器 API。這是它自己的主題；請參閱[編譯擴展](/building-extensions/compiled/overview)。

## 另請參閱

- [Scratch 對象 API](/building-extensions/apis/scratch-api)
- [渲染器 API](/building-extensions/apis/renderer-api)
- [編譯擴展](/building-extensions/compiled/overview)
- [運行時參考](/api-reference/runtime)
- [線程參考](/api-reference/threads)
