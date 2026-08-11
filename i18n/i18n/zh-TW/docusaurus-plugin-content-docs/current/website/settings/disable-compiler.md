---
title: 禁用編譯器
sidebar_position: 15
---

# 禁用編譯器

RemixWarp 的[編譯器](/website/javascript)會將您的積木轉換為 JavaScript，使它們比原版 Scratch 運行得快得多。此選項將其關閉，回退到像 Scratch 一樣逐個解釋積木。可以在[編輯器設置](/user-guide/settings)或通過 [`nocompile` URL 參數](/website/url-parameters) 切換。

::::warning
除非您確切知道為什麼需要，否則不要更改此項。禁用編譯器會使項目慢得多。
::::

禁用它的兩個合理原因：

- **調試編譯器 bug。** 如果腳本在 RemixWarp 中的行為與在 Scratch 中不同，關閉編譯器可以判斷編譯器是否是原因。
- **編輯。** 關閉編譯器後，腳本更改會在編輯時立即生效，有些人在構建時更喜歡這樣。"在編輯器中禁用編譯器"插件默認就是這麼做的，僅在編輯器中，讓播放器保持快速。

## 另請參閱

- [JavaScript 與編譯器](/website/javascript)
- [插件](/user-guide/addons)
- [編輯器設置](/user-guide/settings)
