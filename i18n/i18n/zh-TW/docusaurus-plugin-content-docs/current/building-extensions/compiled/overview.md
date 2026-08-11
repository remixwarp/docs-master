---
title: 編譯擴展概覽
sidebar_position: 1
---

# 編譯擴展

RemixWarp 不逐積木解釋項目。它**編譯**它們：積木被轉換為 JavaScript，瀏覽器以原生速度運行。普通擴展積木是編譯代碼調用的函數，這對大多數事情來說足夠快，但仍然是一種解釋器風格的調用。

編譯擴展更進一步。它告訴編譯器如何將您的積木*內聯*轉換為 JavaScript，因此完全沒有對您的函數的調用。對於數學積木，這就是"調用返回 `Math.pow(a, b)` 的擴展"和直接向腳本中發射 `Math.pow(a, b)` 之間的區別。

## 何時值得

編譯積木只在積木很小且運行很多時有幫助：數學、字符串處理和其他緊密循環操作。它對以真實工作為主的積木（網絡請求、繪製、等待）沒有作用，並且它增加了複雜性。

在以下情況使用編譯積木：

- 操作便宜但每幀被調用數千次，並且解釋器開銷出現在性能分析中。
- 您可以將積木表示為短的 JavaScript 表達式。

當積木做任何實質性的工作時、在原型設計時，或額外複雜性不值當時，請堅持使用[普通擴展](/building-extensions/introduction)。

## 要求

- 編譯擴展必須以[非沙箱](/building-extensions/unsandboxed)方式運行；它們使用只在主頁面中存在的 `Scratch.vm.exports`。
- 它們依賴 RemixWarp 的編譯器，因此它們在 RemixWarp 和[打包器](/packager/overview)中運行，但在標準 Scratch 中不運行。
- 您總是提供普通的 `func` 回退，使積木在編譯器關閉時仍然工作（例如當監視器讀取報告積木時，或如果用戶禁用編譯器）。

## 兩種做法

RemixWarp 在 `Scratch.vm.exports` 上暴露兩個編譯器入口點：

- **`vm.exports.compiler.register(...)`** 是受支持的、穩定的方式。您為每個積木註冊一個返回 JavaScript 源字符串的小 `compile` 函數。本節的其餘部分教的就是這個。
- **`vm.exports.i_will_not_ask_for_help_when_these_break()`** 為*舊的* TurboWarp 風格（修補編譯器內部生成器）返回一個兼容墊片。它的存在是為了讓較舊的編譯擴展繼續工作。這個名字是一個字面警告：它不受支持，按約定沒有文檔，並且可能在任何版本中損壞。只用它來讓遺留擴展運行；用 `compiler.register` 編寫新的。請參閱[修補編譯器](/building-extensions/compiled/patching)。

## 開始

先閱讀[普通擴展開發](/building-extensions/introduction)；編譯積木仍然是一個帶編譯器入口的普通積木。然後繼續[擴展結構](/building-extensions/compiled/structure)。
