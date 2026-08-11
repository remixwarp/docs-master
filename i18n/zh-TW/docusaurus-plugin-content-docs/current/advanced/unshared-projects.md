---
title: 未共享項目
sidebar_position: 5
---

# 未共享項目

Scratch 上未共享的項目無法在 RemixWarp、打包器或任何其他第三方網站中打開。這是 Scratch 的限制，不是 RemixWarp 的，並且在不危及賬戶安全的情況下沒有任何辦法繞過。

::::warning
任何非 scratch.mit.edu 的網站，如果索要您的 Scratch 密碼，都是詐騙，即使它聲稱能讓您打開未共享的項目。您的賬戶會被盜。這條規則沒有任何例外。
::::

## 為什麼會這樣

從 Scratch API 下載項目需要一個臨時的"項目令牌"。對於未共享的項目，該令牌只能由項目所有者獲得，並且幾分鐘後過期。即使您在同一瀏覽器中登錄了 Scratch，RemixWarp 也無法讀取該令牌，因此無法下載項目數據。

這是 Scratch 團隊有意做出的更改，讓未共享項目真正私密。在此之前，"未共享"項目實際上對任何知道 ID 的人都是公開的，考慮到其中許多項目包含個人信息，這是一個真正的隱私問題。保護它們是正確的決定。

## 應該怎麼做

**測試自己的項目。** 在 Scratch 編輯器中使用文件，然後保存到電腦下載 `.sb3`，然後在 RemixWarp 中使用文件，然後從電腦加載打開它。許多人主要在 RemixWarp 中工作，並將完成的 `.sb3` 上傳回 Scratch。這樣做時請保留備份。

**協作。** 在 Scratch 上共享項目。共享未完成的工作完全可以。如果您想與他人實時編輯，RemixWarp 還內置了完全不依賴 Scratch 的[協作](/editor/collaboration)。

**嵌入。** 在 Scratch 上共享項目，或下載 `.sb3` 並使用[RemixWarp 打包器](/packager/overview)將其轉換為可以[嵌入](/packager/embedding)的獨立文件。

## 面向工具開發者

本部分面向構建自己的 Scratch 相關工具的人。要下載共享項目，您首先獲取其元數據以獲得項目令牌，然後使用該令牌獲取數據：

1. `GET https://api.scratch.mit.edu/projects/<id>` 並讀取 `project_token` 字段。
2. `GET https://projects.scratch.mit.edu/<id>?token=<token>` 獲取項目 JSON 或 SB3。

瀏覽器不能直接調用 `api.scratch.mit.edu`，因為它不發送 [CORS](/advanced/cors) 頭，因此瀏覽器端代碼需要 CORS 代理；服務器端代碼（Node.js）不受 CORS 約束，可以直接調用。有關處理這一切的現成下載器，請參閱 [sb-downloader](https://github.com/forkphorus/sb-downloader)。

## 另請參閱

- [協作](/editor/collaboration)
- [RemixWarp 打包器](/packager/overview)
- [CORS](/advanced/cors)
