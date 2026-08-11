---
title: Scratch 對象 API
sidebar_position: 1
---

# Scratch 對象 API

全局 `Scratch` 對象是擴展與 RemixWarp 對話的方式。它攜帶註冊函數、類型常量、轉換輔助工具，以及（對於非沙箱擴展）對 VM 和權限 API 的直接訪問。

沙箱擴展得到一個受限的 `Scratch`；VM、渲染器和積木工具僅限非沙箱。

## 註冊與結構

```js
(function(Scratch) {
  'use strict';
  class MyExtension {
    getInfo() {
      return {
        id: 'myextension',
        name: 'My Extension',
        blocks: [
          {
            opcode: 'myBlock',
            blockType: Scratch.BlockType.REPORTER,
            text: 'convert [VALUE] to number',
            arguments: { VALUE: { type: Scratch.ArgumentType.STRING, defaultValue: '42' } }
          }
        ]
      };
    }
    myBlock(args) {
      return Scratch.Cast.toNumber(args.VALUE);
    }
  }
  Scratch.extensions.register(new MyExtension());
})(Scratch);
```

- `Scratch.extensions.register(instance)`：註冊您的擴展。恰好調用一次。
- `Scratch.extensions.unsandboxed`：以非沙箱方式運行時為 `true`。在使用任何僅非沙箱的 API 之前檢查它。

## 類型常量

### Scratch.BlockType

| 常量 | 值 | 含義 |
|:--|:--|:--|
| `COMMAND` | `command` | 堆疊積木，無返回值 |
| `REPORTER` | `reporter` | 返回字符串或數字的圓形積木 |
| `BOOLEAN` | `Boolean` | 返回真/假的六邊形積木 |
| `HAT` | `hat` | 有條件地啟動堆棧（請參閱[事件和帽子](/building-extensions/hats)） |
| `EVENT` | `event` | 在事件上啟動堆棧；沒有函數 |
| `CONDITIONAL` | `conditional` | `如果`/`否則` 風格 C 積木（請參閱[自定義 C 積木](/building-extensions/custom-c-blocks)） |
| `LOOP` | `loop` | `重複執行`/`重複執行無限次` 風格 C 積木 |
| `BUTTON` | `button` | 積木區按鈕，不是真正的積木 |
| `LABEL` | `label` | 積木區中的文本標籤，不是真正的積木 |
| `XML` | `xml` | 原始 Blockly XML |

### Scratch.ArgumentType

`STRING`、`NUMBER`、`BOOLEAN`、`COLOR`、`ANGLE`、`MATRIX`、`NOTE`、`COSTUME`、`SOUND`、`IMAGE`。每個接受什麼請參閱[處理輸入](/building-extensions/inputs)。

### Scratch.TargetType

`SPRITE`（`'sprite'`）和 `STAGE`（`'stage'`），與積木的 `filter` 一起使用。

## Scratch.Cast

Scratch 語義的轉換。完整細節在[實用 API 頁面](/building-extensions/apis/utility-apis)。

```js
Scratch.Cast.toNumber('3.14');   // 3.14
Scratch.Cast.toString(42);       // '42'
Scratch.Cast.toBoolean('false'); // false
Scratch.Cast.compare('10', '9'); // > 0
```

## Scratch.vm（僅非沙箱）

VM 實例。完整的表面請參閱[VM API 頁面](/building-extensions/apis/vm-api)。

```js
const vm = Scratch.vm;
const runtime = vm.runtime;

vm.greenFlag();
vm.stopAll();
vm.setTurboMode(true);

runtime.targets;               // 所有角色和舞臺
runtime.getTargetForStage();   // 舞臺
vm.editingTarget;              // 編輯器中選中的角色

runtime.on('PROJECT_RUN_START', () => { /* ... */ });
```

## Scratch.renderer（僅非沙箱）

WebGL 渲染器。請參閱[渲染器 API 頁面](/building-extensions/apis/renderer-api)。

```js
const renderer = Scratch.renderer;
renderer.draw();
const canvas = renderer.canvas;
```

## 積木工具（僅非沙箱）

非沙箱積木函數接收第二個參數 `util`，只在積木運行時有效（請參閱[非沙箱擴展](/building-extensions/unsandboxed)）。

```js
myBlock(args, util) {
  const target = util.target;   // 運行積木的角色
  const runtime = util.runtime; // 運行時
  const thread = util.thread;   // 運行中的線程
  const frame = util.stackFrame; // 此積木調用的暫存空間
}
```

常見用途：

```js
// 目標屬性
util.target.x; util.target.y; util.target.direction; util.target.size;
util.target.setXY(100, 50);
util.target.setDirection(90);

// 變量和列表（變量類型為 ''，列表類型為 'list'）
const v = util.target.lookupVariableByNameAndType('score', '');
if (v) v.value = 100;

// 啟動帽子/事件腳本（請參閱事件和帽子頁面）
util.startHats('event_whenbroadcastreceived', { BROADCAST_OPTION: 'go' });

// C 積木分支（請參閱自定義 C 積木頁面）
util.startBranch(1, true);
```

## 權限 API（僅非沙箱）

非沙箱擴展在接觸網絡或外部世界之前必須請求。為什麼以及如何請參閱[非沙箱擴展](/building-extensions/unsandboxed)。

```js
// 網絡
if (await Scratch.canFetch(url)) { /* WebSocket、Image 等 */ }
const res = await Scratch.fetch(url);

// 窗口 / 導航
if (await Scratch.canOpenWindow(url)) { /* ... */ }
await Scratch.openWindow(url);
if (await Scratch.canRedirect(url)) { /* ... */ }
await Scratch.redirect(url);

// 設備
await Scratch.canRecordAudio();
await Scratch.canRecordVideo();
await Scratch.canReadClipboard();
await Scratch.canNotify();
await Scratch.canGeolocate();
```

## 翻譯

`Scratch.translate` 標記字符串以供翻譯：

```js
const message = Scratch.translate({
  id: 'myextension.hello',
  default: 'Hello {name}!',
  description: 'Greeting'
}, { name: args.NAME });
```

## 直接編輯 Blockly

要進行深度編輯器自定義，您可以接觸全局 `ScratchBlocks` 對象。詳情請參閱[GUI API](/api-reference/gui-api)。

## 另請參閱

- [VM API](/building-extensions/apis/vm-api)
- [渲染器 API](/building-extensions/apis/renderer-api)
- [音頻 API](/building-extensions/apis/audio-api)
- [實用 API](/building-extensions/apis/utility-apis)
