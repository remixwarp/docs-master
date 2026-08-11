---
title: 你好，世界！
sidebar_position: 2
---

# 你好，世界！

這裡有一個完整的擴展，它添加一個積木，一個返回"World!"的報告積木。將其保存為 `hello-world.js`，放在您的[開發服務器](/building-extensions/introduction)可以提供服務的位置（[下載](/example-extensions/hello-world.js)）。

```js
class HelloWorld {
  getInfo() {
    return {
      id: 'helloworld',
      name: 'It works!',
      blocks: [
        {
          opcode: 'hello',
          blockType: Scratch.BlockType.REPORTER,
          text: 'Hello!'
        }
      ]
    };
  }

  hello() {
    return 'World!';
  }
}

Scratch.extensions.register(new HelloWorld());
```

在編輯器中加載它："添加擴展"，滾動到底部，"自定義擴展"，然後輸入您本地服務器的 URL（或粘貼代碼 / 選擇文件）。現在**不要**勾選"不進入沙箱運行擴展"。

片刻之後，一個名為"It works!"的擴展出現在積木區中。如果沒有，請打開開發者控制台查找錯誤。常見原因是 JavaScript 語法錯誤、運行時錯誤（兩者都顯示在控制台中），或廣告攔截器阻止了對 localhost 的請求。

現在讓我們按運行順序逐段瀏覽該文件。

## 註冊

```js
Scratch.extensions.register(new HelloWorld());
```

`Scratch` 是 RemixWarp 交給每個擴展的全局對象。`Scratch.extensions.register` 是您的擴展告訴 RemixWarp 它存在的方式。類名（`HelloWorld`）無關緊要，也不需要唯一。

**恰好**調用一次 `register()`。如果您從不調用它，RemixWarp 會永遠等待您的擴展加載。如果您調用多次，行為是未定義的。

## getInfo()

```js
getInfo() {
  return {
    id: 'helloworld',
    name: 'It works!',
    blocks: [
      {
        opcode: 'hello',
        blockType: Scratch.BlockType.REPORTER,
        text: 'Hello!'
      }
    ]
  };
}
```

調用 `register()` 後，RemixWarp 會在您的對象上調用 `getInfo()` 來了解擴展。它必須返回一個描述擴展的對象：

| 字段 | 類型 | 描述 |
|:-:|:-:|:--|
| `id` | string | 此擴展的唯一 ID。沒有兩個已加載的擴展可以共享一個 ID。只使用 `a-z` 和 `0-9`，不要用空格或符號。它成為每個積木內部操作碼的一部分，並且一旦項目使用它，就**絕不能更改**。 |
| `name` | string | 積木區中顯示的名稱。省略時默認為 `id`。 |
| `blocks` | array | 此擴展提供的積木。 |

每個積木對象通常具有：

| 字段 | 類型 | 描述 |
|:-:|:-:|:--|
| `opcode` | string | 積木運行時運行的方法名。`opcode: 'hello'` 運行 `this.hello()`。在擴展內必須唯一。 |
| `blockType` | `Scratch.BlockType.*` | 積木的形狀和行為。見下文。 |
| `text` | string | 積木上顯示的標籤。參數佔位符放在這裡（下一頁）。 |
| `arguments` | object | 可選。[處理輸入](/building-extensions/inputs)中介紹。 |

常見的積木類型：

| 值 | 形狀 | 示例 |
|:-:|:--|:--|
| `Scratch.BlockType.COMMAND` | 堆疊積木，無返回值 | 移動 10 步 |
| `Scratch.BlockType.REPORTER` | 返回字符串或數字的圓形積木 | x 座標 |
| `Scratch.BlockType.BOOLEAN` | 返回真/假的尖形積木 | 鼠標按下? |
| `Scratch.BlockType.HAT` | 在條件上啟動腳本 | 當響度 > 10 |
| `Scratch.BlockType.EVENT` | 在事件上啟動腳本 | 當角色被點擊時 |

`HAT` 和 `EVENT` 在[事件和帽子](/building-extensions/hats)中介紹。`CONDITIONAL` 和 `LOOP`（C 形積木）在[自定義 C 積木](/building-extensions/custom-c-blocks)中介紹。

## 積木函數

```js
hello() {
  return 'World!';
}
```

這是由 `opcode: 'hello'` 命名的方法。報告積木返回字符串或數字；布爾積木返回 `true` 或 `false`。不要返回 `null`、`undefined`、數組或對象；這些不是有效的積木值，會導致問題。

## 快速迭代

更改文件，然後重新加載編輯器頁面。有兩件事可以讓這更快：

- `?extension=` URL 參數會自動加載擴展。如果您的文件在 `http://localhost:8080/hello-world.js`，打開 `https://remixwarp.pages.dev/editor?extension=http://localhost:8080/hello-world.js` 來加載它，無需經過素材庫。
- 如果重新加載後更改沒有顯示，請使用瀏覽器的"硬刷新"（忽略緩存重新加載）。

## 練習

1. 將積木改為返回您最喜歡的數字而不是字符串，並重命名積木文本以匹配。
2. 更改積木的操作碼（記住也要重命名方法）。
3. 添加第二個 `blockType: Scratch.BlockType.BOOLEAN` 的積木，隨機返回 `true` 或 `false`。

## 下一步

接下來，[讓積木接受輸入](/building-extensions/inputs)。
