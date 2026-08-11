---
title: 高質量畫筆
sidebar_position: 9
---

# 高質量畫筆

默認情況下，畫筆層以 480x360 繪製並拉伸以適合舞臺，因此當舞臺較大時，畫筆圖案可能看起來有鋸齒。高質量畫筆改為以舞臺的真實分辨率渲染畫筆層，並禁用部分座標舍入，讓畫筆線條落在您期望的位置。可以在[編輯器設置](/editor/settings)或通過 [`hqpen` URL 參數](/advanced/url-parameters) 啟用。

::::caution
高質量畫筆會顯著降低性能，尤其是在全屏模式下，因為每幀需要繪製更多像素。並非所有項目開啟它都會更好看，因此發佈前請先對比。
::::

它與[自定義舞臺大小](/advanced/custom-stage-size)天然搭配，因為那時低默認畫筆分辨率最明顯。

## 另請參閱

- [自定義舞臺大小](/advanced/custom-stage-size)
- [畫筆擴展](/extensions/pen)
- [編輯器設置](/editor/settings)
