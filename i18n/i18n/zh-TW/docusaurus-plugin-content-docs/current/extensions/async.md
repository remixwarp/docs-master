---
title: 等待非即時的事物
sidebar_position: 4
---

# 等待非即時的事物

有時積木必須在腳本繼續之前等待異步操作。網絡請求是經典示例：無論您的連接多快，請求都不可能是即時的。

積木表示"我還沒完成"的方式是返回一個 [Promise](https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Reference/Global_Objects/Promise)。RemixWarp 在運行下一個積木之前等待 Promise 解析，並且可能同時運行其他腳本（[下載](/example-extensions/async.js)）：

```js
class AsyncExtension {
  getInfo() {
    return {
      id: 'asyncexample',
      name: 'Async Blocks',
      blocks: [
        {
          opcode: 'wait',
          text: 'wait [TIME] seconds',
          blockType: Scratch.BlockType.COMMAND,
          arguments: {
            TIME: { type: Scratch.ArgumentType.NUMBER, defaultValue: 1 }
          }
        },
        {
          opcode: 'fetch',
          text: 'fetch [URL]',
          blockType: Scratch.BlockType.REPORTER,
          arguments: {
            URL: {
              type: Scratch.ArgumentType.STRING,
              defaultValue: 'https://extensions.bilup.org/hello.txt'
            }
          }
        }
      ]
    };
  }

  wait(args) {
    return new Promise((resolve) => {
      setTimeout(resolve, args.TIME * 1000);
    });
  }

  fetch(args) {
    return fetch(args.URL)
      .then((response) => response.text())
      .catch((error) => {
        console.error(error);
        return 'Uh oh! Something went wrong.';
      });
  }
}
Scratch.extensions.register(new AsyncExtension());
```

異步積木在 `getInfo()` 中聲明的方式與其他積木完全一樣。唯一改變的是函數返回什麼。

## 關於兩個積木的說明

`wait` 積木大致是 Scratch 內置的 `wait` 積木。`setTimeout` 不使用 Promise，因此我們手動構造一個並在超時內解析它。因為 `wait` 是命令（無返回值），它解析時不帶任何值。

`fetch` 積木請求一個 URL，就像畫廊中的"Fetch"擴展一樣。`fetch()` 已經返回一個 Promise，因此我們在它上面鏈接，而不是製作新的。報告積木必須返回字符串、數字或布爾值的規則仍然適用，因此我們調用 `.text()` 將 `Response` 對象變成字符串。

## 總是處理錯誤

任何可能拒絕的 Promise 都需要 `.catch()`。您如何處理失敗取決於積木，但報告積木仍應返回有效的字符串或數字；返回錯誤消息（如上）是合理的默認值。未處理的拒絕可能讓腳本卡住。

::::info
在[非沙箱擴展](/extensions/unsandboxed)中，您應該使用 `Scratch.fetch(url)` 而不是這裡顯示的普通 `fetch(url)`，以便尊重用戶的獲取權限設置。在沙箱擴展中，普通 `fetch` 沒問題。
::::

## 練習

1. 寫一個命令積木，第一次運行等待 100 毫秒，第二次 200 毫秒，第三次 300 毫秒，依此類推。

## 下一步

即使不返回 Promise 的積木也不是真正即時的，並且無法接觸許多 API。要理解為什麼，我們需要談談[沙箱](/extensions/sandbox)。
