---
title: 自定義舞臺大小
sidebar_position: 8
---

# 自定義舞臺大小

RemixWarp 可以將舞臺從 Scratch 默認的 480x360（4:3）更改為任何其他尺寸，可以從[編輯器設置](/editor/settings)或 [`size` URL 參數](/advanced/url-parameters)（`size=640x360`）進行設置。

::::caution
大多數項目並非針對不同的舞臺大小而設計，更改後佈局可能無法正確顯示。
::::

例如，`640x360` 提供寬屏 16:9 舞臺。`1280x720` 或 `1920x1080` 等更高分辨率也有效，但通常最好以相同寬高比的較低分辨率創作，讓全屏模式負責放大。非常大的舞臺可能在某些顯示器上無法完整顯示，而且渲染成本更高。

項目可以在運行時讀取當前舞臺大小，因此定位或縮放的腳本可以自適應。如果您希望打包構建中的舞臺自動跟隨窗口或全屏大小，請參閱[動態舞臺縮放](/packager/dynamic-stage-resize)。

## 另請參閱

- [高質量畫筆](/advanced/high-quality-pen)
- [動態舞臺縮放](/packager/dynamic-stage-resize)
- [編輯器設置](/editor/settings)
