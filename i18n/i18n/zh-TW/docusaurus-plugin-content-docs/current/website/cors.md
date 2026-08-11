---
title: CORS
sidebar_position: 6
---

# CORS：為什麼您的 fetch 積木不工作

如果您使用 fetch、HTTP 或網絡擴展，而請求總是失敗，即使您已允許，原因幾乎總是 **CORS**。這是瀏覽器安全功能，不是 RemixWarp 或擴展的 bug。

## 什麼是 CORS

CORS（跨源資源共享）是網站聲明是否允許其他網站讀取其響應的方式。它解決的問題很簡單：有些網站想阻止其他網站的訪問（想像一下，您訪問的任何頁面都能在您登錄時讀取您的銀行賬戶），有些網站則想允許訪問。

默認情況下，網站**不**允許跨源訪問。網站必須通過發送 `Access-Control-Allow-Origin` 頭來主動選擇開放。Scratch API 的部分內容選擇了開放，這就是 RemixWarp 能從 Scratch 加載項目的原因。當網站沒有選擇開放時，瀏覽器會阻止 RemixWarp 讀取響應，您會得到一個通用的網絡錯誤。

這是由瀏覽器本身強制執行的。RemixWarp 無法在網頁上覆蓋它。

## 如何解決

這取決於您獲取該 URL 的原因。

- **使用不同的 URL。** 如果您只是託管靜態文件，請將它們移到支持帶 CORS 的直接下載的主機上。如果一個 API 阻止 CORS，請檢查是否有替代 API 允許它。
- **使用 CORS 代理。** CORS 代理是另一個服務器，它為您獲取 URL 並重新發送帶 CORS 頭的響應。公共代理確實存在，但通常很短命，因為運營成本高且被嚴重濫用。RemixWarp 不提供代理。
- **在桌面版或打包構建中運行項目。** 這些不受瀏覽器 CORS 規則約束（見下文）。

## 桌面版和打包項目

使用[02Engine Packager](/packager/overview)打包為 Electron 應用的項目默認繞過 CORS，就像原生應用一樣，因此 fetch 積木可以訪問任何 URL。

打包後以普通 HTML 文件在瀏覽器中運行的項目仍受正常瀏覽器 CORS 規則約束，因為它們仍然是網站。

## 如果您運行服務器

如果您控制被 fetch 的服務器，並且希望網站能夠讀取它，請在您想公開的響應上設置 `Access-Control-Allow-Origin` 頭為 `*`。搜索您的 Web 服務器或框架的名稱加 "cors" 會找到示例。

## 另請參閱

- [畫筆擴展](/extensions/pen) 和其他[擴展](/extensions/overview)
- [02Engine Packager](/packager/overview)
