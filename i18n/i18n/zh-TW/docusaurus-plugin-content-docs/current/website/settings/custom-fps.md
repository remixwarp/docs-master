---
title: 自定義 FPS
sidebar_position: 7
---

# 自定義 FPS

幀率（每秒幀數）控制您的腳本每秒運行多少次。Scratch 以 30 FPS 運行。RemixWarp 允許您更改此設置，最常見的是 60 FPS，可以從[編輯器設置](/user-guide/settings)或 [`fps` URL 參數](/website/url-parameters) 中進行設置。

`0` 值很特殊：項目以顯示器的刷新率運行，而不是固定間隔。在 `0` 時，當項目的標籤頁隱藏時，腳本可能會停止運行。

## 大多數項目需要修改才能在更高 FPS 下正常工作

提高幀率會讓腳本運行得更頻繁，因此每幀移動固定距離的內容會移動得更快。考慮 `重複執行 { 移動 1 步 }`：在 30 FPS 下角色每秒移動 30 步，但在 60 FPS 下每秒移動 60 步，快了兩倍。

如果您只想獲得更流暢的運動而不改變遊戲速度，請使用[插值](/website/interpolation)而不是提高幀率。插值讓腳本保持正常速率，並在其間平滑視覺效果。

要讓項目真正獨立於幀率，請使用**增量時間**：測量自上一幀以來經過的真實時間，並按它縮放移動。這是常見的遊戲開發技術，通常需要重構您的移動腳本。

- [增量計時（維基百科）](https://en.wikipedia.org/wiki/Delta_timing)

## 另請參閱

- [插值](/website/interpolation)
- [URL 參數](/website/url-parameters)
- [編輯器設置](/user-guide/settings)
