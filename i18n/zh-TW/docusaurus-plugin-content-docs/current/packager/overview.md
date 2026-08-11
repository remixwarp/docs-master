---
title: 概覽
sidebar_position: 1
---

# RemixWarp 打包器

RemixWarp 打包器將 Scratch 或 RemixWarp 項目變成獨立程序：單個 HTML 文件、zip，或 Windows、macOS、Linux 的原生可執行文件。輸出不需要編輯器或互聯網連接即可運行，並且捆綁了 RemixWarp 快速的編譯運行時。

在 [packager.02engine.org](https://packager.02engine.org/) 使用它。

它與 HTMLifier 或 forkphorus 打包器扮演相同的角色，但提供更多輸出格式，並對加載屏幕、控件和運行時設置擁有更多控制。

## 您可以做什麼

- **將項目作為單個文件分享。** 給某人一個 HTML 文件，他們可以在任何瀏覽器中打開，周圍沒有 RemixWarp 品牌。
- **發佈桌面應用。** 打包為像原生程序一樣運行的 Electron、NW.js 或 WKWebView 可執行文件。
- **嵌入您完全控制的項目。** [嵌入打包文件](/packager/embedding)，而不是依賴託管的嵌入。
- **離線或在受限網絡上運行。** 請參閱[離線打包器](/packager/offline)。

## 將項目放入打包器

您有幾個選項：

- 輸入 Scratch 項目 ID 或直接項目 URL。
- 從電腦上傳 `.sb3` 文件。
- 直接從編輯器發送當前項目。請參閱[編輯器集成](/packager/editor-integration)。

請記住，[未共享的 Scratch 項目](/advanced/unshared-projects)不能通過 ID 加載；請下載 `.sb3` 並改為上傳。

## 常用設置

打包器公開與編輯器相同的大多數運行時選項，包括[自定義 FPS](/advanced/custom-fps)、[插值](/advanced/interpolation)、[高質量畫筆](/advanced/high-quality-pen)和[自定義舞臺大小](/advanced/custom-stage-size)。它還添加打包器特有的功能：

- [動態舞臺縮放](/packager/dynamic-stage-resize) 讓舞臺跟隨窗口或全屏大小。
- [特殊雲行為](/packager/special-cloud-behaviors) 用於具有特殊名稱的雲變量。

## 另請參閱

- [嵌入打包項目](/packager/embedding)
- [編輯器集成](/packager/editor-integration)
- [離線打包器](/packager/offline)
- [我可以出售打包項目嗎?](/packager/commercial-use)
