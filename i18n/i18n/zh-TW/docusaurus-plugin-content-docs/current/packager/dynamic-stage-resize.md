---
title: 動態舞臺縮放
sidebar_position: 4
slug: /packager/dynamic-stage-resize
---

# 動態舞臺縮放

::::info
這是[RemixWarp 打包器](/packager/overview)的選項。
::::

動態舞臺縮放讓舞臺匹配它被顯示的任何大小和寬高比，而不是固定的[舞臺大小](/advanced/custom-stage-size)。

舞臺不被縮放，它的實際尺寸會改變。如果用戶在 1920x1080 的顯示器上全屏，舞臺變成 1920x1080。如果他們將窗口縮小到 1x1，舞臺變成 1x1，因此請在項目中添加最小尺寸檢查，以避免退化情況。

## 使項目兼容

幾乎沒有項目開箱即用地處理這一點。要支持它：

1. 首先讓項目在[自定義舞臺大小](/advanced/custom-stage-size)下工作。
2. 然後將舞臺大小檢測移入每幀運行的循環中，並根據每幀的當前大小重新定位所有內容。這不是優雅的，但足夠快，也是最可靠的方法。

## 另請參閱

- [自定義舞臺大小](/advanced/custom-stage-size)
- [打包器概覽](/packager/overview)
