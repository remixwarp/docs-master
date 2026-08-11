---
title: 特殊雲行為
sidebar_position: 5
slug: /packager/special-cloud-behaviors
---

# 特殊雲行為

::::info
這是[RemixWarp 打包器](/packager/overview)的選項。
::::

"特殊雲行為"是一個選項（默認關閉），它給具有特殊名稱的[雲變量](/advanced/cloud-variables)特殊能力，使打包項目可以與它運行的頁面交互。它基於 [HTMLifier 中的相同功能](https://github.com/SheepTester/htmlifier/wiki/Special-cloud-behaviours)，您可以在打包器的"雲變量"部分啟用它。

要使用一個，請創建一個名稱與下面列出完全相同的普通雲變量。例如，對於 `☁ url`，創建一個名為 `url` 的雲變量。

啟用特殊雲行為會覆蓋這些名稱的正常雲處理，因此像 `☁ username` 這樣的變量永遠不會在本地存儲或與其他玩家同步。

## 只讀

### ☁ url
設置為頁面當前的 URL。寫入它不做任何事情。

### ☁ pasted
當用戶在頁面上粘貼文本時（例如用 Ctrl+V），粘貼的文本會放在這裡。

## 操作

### ☁ redirect
將其設置為一個 URL，當前標籤頁會導航到那裡。

### ☁ open link
將其設置為一個 URL，在新標籤頁中打開該 URL。瀏覽器彈出窗口攔截器可能會阻止這一點。

### ☁ username
更改它會在偵測分類中更改 `用戶名` 積木返回的值。

### ☁ set clipboard
更改它會嘗試將文本複製到用戶的剪貼板。瀏覽器並不總是允許。

### ☁ room id
更改它會改變用於同步雲變量的項目 ID。如果原始 ID 是 `1234`，您將 `☁ room id` 設置為 `xyz`，同步 ID 變成 `1234-xyz`。將其設置回空字符串以恢復原始值。只有共享房間 ID 的玩家彼此同步，這使它成為無需額外變量的簡單服務器選擇器。重新連接可能需要幾秒鐘。這不影響本地存儲的雲變量。

## 運行代碼

### ☁ eval

::::warning
這需要單獨的"不安全的特殊雲行為"選項。不安全的行為讓打包項目在正常項目沙箱之外運行任意代碼。根據您打包的內容，這可以給項目對其運行的電腦的完全控制權，包括安裝惡意軟件。除非您信任該項目並實際使用此功能，否則請保持關閉。
::::

設置 `☁ eval`，其值會作為 JavaScript 運行。結果寫入 `☁ eval output`，錯誤寫入 `☁ eval error`。如果代碼返回一個 [Promise](https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Reference/Global_Objects/Promise)，解析值或拒絕錯誤會在它結算時寫入這些變量。設置 `☁ eval` 會立即返回，因此輸出變量可能不會在同一幀更新。

## 另請參閱

- [雲變量](/advanced/cloud-variables)
- [打包器概覽](/packager/overview)
