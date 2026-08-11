---
title: JavaScript 與編譯器
sidebar_position: 2
---

# JavaScript 與編譯器

JavaScript 以三種方式出現在 RemixWarp 中：**編譯器**會自動將您的積木轉換為 JavaScript 以提高速度，**補丁擴展**提供 `js (...)` 積木讓您在項目中運行自己的 JavaScript，**擴展系統**讓您用 JavaScript 編寫自己的完整積木。本頁涵蓋這三者。

## 編譯器

每次項目運行時，RemixWarp 都會將您的腳本編譯為瀏覽器可以直接運行的 JavaScript，而不是逐個解釋積木。這是項目在 RemixWarp 中比原版 Scratch 運行快得多的主要原因。它是自動發生的，無需開啟任何東西，結果與積木在 Scratch 中的行為相同（除了更快）。

腳本在首次運行時編譯。如果項目似乎在腳本首次觸發時短暫停頓，那就是編譯發生了一次；它不會重複。

您幾乎不需要考慮編譯器。您可能需要考慮它的兩種情況：

- **調試編譯器 bug。** 如果腳本在 RemixWarp 中的行為與在 Scratch 中不同，您可以關閉編譯器檢查是否是編譯器的錯。請參閱[禁用編譯器](/website/disable-compiler)。
- **查看生成的代碼**（見下文）。

## 在項目內部運行 JavaScript

[**補丁擴展**](/extensions/patching) 添加了可運行您在項目中直接編寫的 JavaScript 的積木：

- **報告型** `js (...)`，返回 JavaScript 表達式的值，
- **布爾型** `js (...)`，用於條件判斷，
- **命令型** `js (...)`，運行一條語句。

由於 JavaScript 被拼接到編譯輸出中，這些積木只在編譯器開啟時工作；禁用編譯器後它們會拋出"補丁積木需要編譯器"。這是直接的"粘貼一些 JavaScript"路徑，與頁面上運行的任何代碼一樣，只運行您理解的 JavaScript。

## 用 JavaScript 編寫自己的積木

如果您需要的不僅僅是一行內表達式（調用 Web API、使用瀏覽器功能或添加可複用的自己的積木），請編寫一個**非沙箱擴展**。非沙箱擴展在與編輯器相同的上下文中運行，可以完全訪問 VM、渲染器以及 `fetch` 和 `localStorage` 等普通瀏覽器 API。

這是真正的編程任務，不是積木。完整指南在[構建擴展](/extensions/introduction)，非沙箱環境的具體細節在[非沙箱擴展](/extensions/unsandboxed)。您可以通過 [`extension` URL 參數](/website/url-parameters#extension) 從 URL 加載擴展：

```
https://remixwarp.pages.dev/?extension=https://example.com/extension.js
```

::::warning
非沙箱擴展以完全訪問權限在頁面上運行。只加載來自可信來源的擴展。惡意擴展可以做您的瀏覽器能做的任何事情。
::::

## 查看生成的 JavaScript

RemixWarp 生成的 JavaScript **不是為人類閱讀或編輯而設計的**。它針對速度和兼容性進行了優化，而不是可讀性。例如，讀取列表項可能編譯為 `(b1.value[(b0.value | 0) - 1] ?? "")`，其中 `b0` 和 `b1` 是內部變量名。沒有格式，也沒有註釋。

如果您仍然想查看，請在啟動項目前打開瀏覽器的 JavaScript 控制台並運行：

```js
vm.enableDebug();
```

每個腳本編譯時，其編譯後的 JavaScript 都會記錄到控制台。要關閉日誌：

```js
vm.disableDebug();
```

如果您想**學習** Scratch 項目在 JavaScript 中會是什麼樣子，編譯器輸出不是合適的工具。請改用像 [Leopard](https://leopardjs.com/) 這樣的項目轉 JavaScript 轉換器，它會產生乾淨、可讀的代碼。

## 使用自定義代碼打包

要將項目作為獨立 HTML 文件或應用發佈，請使用[02Engine Packager](/packager/overview)。打包器將編譯後的運行時與您的項目捆綁在一起，使其在任何地方都能運行，無需編輯器。

## 另請參閱

- [補丁擴展](/extensions/patching)
- [禁用編譯器](/website/disable-compiler)
- [構建擴展](/extensions/introduction)
- [URL 參數](/website/url-parameters)
