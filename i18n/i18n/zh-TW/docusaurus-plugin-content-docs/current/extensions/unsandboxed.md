---
title: 非沙箱擴展
sidebar_position: 6
---

# 非沙箱擴展

非沙箱擴展作為主頁面中的普通 `<script>` 標籤運行，而不是在沙箱中。這讓它們可以訪問 RemixWarp 的內部，以及一組相應的責任。

## 擴展何時以非沙箱方式運行

RemixWarp 決定如何加載每個擴展：

- **從文件或粘貼的代碼加載**：自定義擴展對話框有一個"不進入沙箱運行擴展"複選框。由您選擇。
- **從 URL 加載**：只有當 URL 恰好以下面一個受信任前綴開頭時，它才自動以非沙箱方式運行：
  - `https://extensions.bilup.org/`
  - `https://extensions.turbowarp.org/`
  - `http://localhost:8000/`

  任何其他 URL 都以沙箱方式加載，除非用戶手動選擇信任它。無法強制任意 URL 以非沙箱方式加載，這是故意的，為了保護用戶免受惡意擴展的侵害。

由於您不控制那兩個畫廊域名，開發期間您從 `http://localhost:8000/` 提供擴展。將您的[本地服務器](/extensions/introduction)指向 8000 端口。它必須恰好是 8000 端口上的 `localhost`；`127.0.0.1` 和 `0.0.0.0` 不會被視為受信任。

## 模板

語法與沙箱擴展幾乎相同，包裹在[立即調用函數表達式（IIFE）](https://developer.mozilla.org/zh-CN/docs/Glossary/IIFE)中並使用嚴格模式：

```js
(function(Scratch) {
  'use strict';
  class MyExtension {
    getInfo() {
      return { /* ... */ };
    }
  }
  Scratch.extensions.register(new MyExtension());
})(Scratch);
```

IIFE 防止非沙箱擴展相互干擾。因為它們共享一個頁面，兩個都聲明全局 `vm` 或 `helper` 的擴展會衝突。將一切包裹在帶 `'use strict'` 的函數中可以讓您的變量保持私有，並給每個擴展自己的 `Scratch` 副本。

您的擴展定義的**每個**變量、函數和類都必須位於 IIFE 內部。這個模板也是向後兼容的：只要不使用任何僅非沙箱的功能，同樣的代碼在沙箱加載時仍然有效。

這裡有一個完整的非沙箱 hello world（[下載](/example-extensions/unsandboxed/hello-world-unsandboxed.js)）：

```js
(function(Scratch) {
  'use strict';

  if (!Scratch.extensions.unsandboxed) {
    throw new Error('This Hello World example must run unsandboxed');
  }

  class HelloWorld {
    getInfo() {
      return {
        id: 'helloworldunsandboxed',
        name: 'Unsandboxed Hello World',
        blocks: [
          { opcode: 'hello', blockType: Scratch.BlockType.REPORTER, text: 'Hello!' }
        ]
      };
    }
    hello() {
      return 'World!';
    }
  }
  Scratch.extensions.register(new HelloWorld());
})(Scratch);
```

在 `http://localhost:8000/hello-world-unsandboxed.js` 提供它並加載那個確切 URL。把它的積木放進一個將它加入列表的 `重複執行 (30)` 中；它會立即運行，而沙箱版本至少要花一秒。

## 新責任

非沙箱代碼與用戶的項目在同一頁面上運行，因此一個錯誤可能造成真正的損害：

- **積木絕不能拋出異常。** 拋出的錯誤可能破壞運行該積木的腳本。
- **報告和布爾積木必須返回有效值**（字符串、數字或布爾值）。返回 `undefined` 可能以令人困惑的方式破壞腳本。
- **積木絕不能陷入無限循環。** 掛起的沙箱擴展通常只是停滯自身；非沙箱的會凍結整個頁面，這可能導致**數據丟失**。

如果您的擴展確實需要非沙箱模式，請響亮且儘早地失敗：

```js
if (!Scratch.extensions.unsandboxed) {
  throw new Error('My Extension must run unsandboxed');
}
```

## 訪問 RemixWarp 內部

頭條功能是 `Scratch.vm`，實際的 VM 對象：

```js
const vm = Scratch.vm;
```

從那裡可以訪問很多東西。記住每個聲明都放在 IIFE 內部：

```js
// 好
(function(Scratch) {
  const vm = Scratch.vm;
  // ...
}(Scratch));

// 壞：洩漏一個全局
const vm = Scratch.vm;
(function(Scratch) { /* ... */ }(Scratch));
```

您的開發者控制台是最好的探索方式：擴展加載後，您可以在那裡檢查 `Scratch` 和 `vm`。[scratch-vm 源碼](/development/project-structure)是存在什麼的參考。

這裡有一個通過 VM 切換渦輪模式的擴展（[下載](/example-extensions/unsandboxed/turbo-mode.js)）：

```js
(function(Scratch) {
  'use strict';

  if (!Scratch.extensions.unsandboxed) {
    throw new Error('This Turbo Mode example must run unsandboxed');
  }
  const vm = Scratch.vm;

  class TurboMode {
    getInfo() {
      return {
        id: 'turbomodeunsandboxed',
        name: 'Turbo Mode',
        blocks: [
          {
            opcode: 'set',
            blockType: Scratch.BlockType.COMMAND,
            text: 'set turbo mode to [ENABLED]',
            arguments: {
              ENABLED: { type: Scratch.ArgumentType.STRING, menu: 'ENABLED_MENU' }
            }
          }
        ],
        menus: {
          ENABLED_MENU: { acceptReporters: true, items: ['on', 'off'] }
        }
      };
    }
    set(args) {
      vm.setTurboMode(args.ENABLED === 'on');
    }
  }
  Scratch.extensions.register(new TurboMode());
})(Scratch);
```

## 積木工具對象

沙箱積木只接收它的參數；它甚至不知道是哪個角色運行了它。非沙箱積木獲得**第二個**參數，習慣上叫 `util`，即 BlockUtility。`util.target` 是運行積木的實際角色（目標）（[下載](/example-extensions/unsandboxed/block-utility-examples.js)）：

```js
getSpriteName(args, util) {
  return util.target.getName();
}
doesVariableExist(args, util) {
  const variable = util.target.lookupVariableByNameAndType(args.NAME.toString(), args.TYPE);
  return !!variable;
}
```

::::warning
每個角色、腳本和積木共享**一個** `util` 對象。RemixWarp 不是每次調用分配新的，而是更新共享對象的屬性。因此 `util` 只在積木運行的準確時刻有效。稍後讀取它（在 `setTimeout`、Promise 回調、事件處理器內部）會得到錯誤的目標。請先把您需要的保存到局部變量中：

```js
// 不可靠：util.target 可能已更改
myBlock(args, util) {
  setTimeout(() => alert(util.target.getName()), 1000);
}

// 可靠：立即捕獲目標
myBlock(args, util) {
  const target = util.target;
  setTimeout(() => alert(target.getName()), 1000);
}
```
::::

一個常見習慣是在 IIFE 頂部為頻繁使用的對象起別名：

```js
const vm = Scratch.vm;
const runtime = vm.runtime;
const Cast = Scratch.Cast;
```

## 需要權限的 API

沙箱擴展被隔離，因此它可以自由使用 `fetch` 和類似的。非沙箱擴展以頁面的全部權力運行，因此它在接觸網絡、打開窗口或重定向前必須請求權限。這讓用戶掌握其隱私的控制權。這些權限檢查還阻止項目偷偷帶入任意 JavaScript（例如 `javascript:` 重定向 URL）。

對某些知名靜態主機的請求可能會自動批准；其他的會提示用戶。不要假設任何一種方式。您的代碼必須處理用戶說不的情況，就像在沒有互聯網連接時那樣行為。

### 網絡：fetch、WebSocket、圖片、音頻

使用 `Scratch.fetch(url)` 而不是 `fetch(url)`。對於其他接觸網絡的 API，將它們放在 `await Scratch.canFetch(url)` 後面：

```js
// 而不是 fetch(url)：
const response = await Scratch.fetch(url);

// WebSocket：
if (await Scratch.canFetch(url)) {
  const ws = new WebSocket(url);
}

// 圖片 / 音頻：
if (await Scratch.canFetch(src)) {
  const image = new Image();
  image.src = src;
}
```

### 打開標籤頁或窗口

使用 `Scratch.openWindow(url)` 而不是 `window.open(url)`。它總是在新標籤頁或窗口中打開。如果您必須自己調用 `window.open`，請將它放在 `await Scratch.canOpenWindow(url)` 後面：

```js
const win = await Scratch.openWindow(url);
// 帶特性：
const win = await Scratch.openWindow(url, 'width=400,height=400');
```

### 重定向頁面

使用 `Scratch.redirect(url)` 而不是 `location.href = url`，或放在 `await Scratch.canRedirect(url)` 後面。

設備訪問存在其他權限檢查：`Scratch.canRecordAudio()`、`canRecordVideo()`、`canReadClipboard()`、`canNotify()`、`canGeolocate()`、`canEmbed()`、`canDownload()`。請參閱 [Scratch API 參考](/extensions/apis/scratch-api)。

## 練習

先不看提示嘗試這些；它教您 VM 是如何佈局的。

1. 一個點擊綠旗的積木。（提示：`vm.greenFlag`。）
2. 一個返回角色 x 座標的報告積木。（提示：`util.target.x`。）
3. 一個將角色移到舞臺中心的命令。（提示：`util.target.setXY(0, 0)`。）

## 下一步

厭倦了硬刷新？讓我們設置[一個更好的開發服務器](/extensions/better-development-server)。
