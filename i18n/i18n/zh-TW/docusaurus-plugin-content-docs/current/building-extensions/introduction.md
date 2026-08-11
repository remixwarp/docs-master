---
title: 自定義擴展簡介
sidebar_position: 1
---

# 自定義擴展簡介

自定義擴展用 JavaScript 為 RemixWarp 添加新積木。本教程從最簡單的擴展逐步構建到功能完整的擴展，一次一個概念。請按順序閱讀各頁，並在繼續之前完成練習；每一頁都假設您理解了上一頁。

如果您只想使用現有積木，您不需要這些。打開編輯器，點擊"添加擴展"按鈕（積木區左下角兩個積木旁邊的加號），然後選擇一個內置擴展。本教程面向想編寫自己的擴展的人。

## "擴展"可以指什麼

這個詞用於幾種不同的事情：

| | 可以訪問 RemixWarp 內部 | 可以通過 URL 加載 |
|:-:|:-:|:-:|
| 內置擴展（畫筆、音樂等） | 是 | 否 |
| 沙箱自定義擴展 | 否 | 是 |
| 非沙箱自定義擴展 | 是 | 是 |

這些頁面只涵蓋**自定義**擴展（沙箱和非沙箱類型）。內置擴展共享相同的積木描述格式，但捆綁在編輯器構建本身中，因此開發它們是涉及 [scratch-vm 源碼](/contributing/project-structure)的不同過程。[沙箱和非沙箱之間的區別](/building-extensions/sandbox)稍後介紹。

## 兼容性

自定義擴展是 RemixWarp 和 TurboWarp 的功能。使用它們的項目不能上傳到 Scratch 網站。它們在 RemixWarp 編輯器中工作，並且可以通過[RemixWarp 打包器](/packager/overview)捆綁到獨立應用或網頁中，打包器總是以非沙箱方式運行擴展。

## 先決條件

編寫擴展需要了解 JavaScript。如果您還不知道 `"1"`（字符串）和 `1`（數字）之間的區別，請先學習 JavaScript；否則擴展開發會非常困難。本教程不教授這門語言。

您還需要瀏覽器的開發者工具。它們通常在右鍵單擊下，然後是"檢查"，或在桌面應用中是 Ctrl+Shift+I（macOS 上是 Option+Command+I）。不打開控制台編寫 JavaScript 是痛苦的，而且您遇到的大多數問題只會在那裡可見。

## 設置開發環境

有幾種方法可以加載您正在開發的擴展。

### 從文件或粘貼的代碼加載（最簡單）

在編輯器中，"添加擴展"，滾動到底部，選擇"自定義擴展"。對話框讓您直接粘貼 JavaScript 或選擇本地文件。這在任何只有文本編輯器的機器上都能工作，但您每次更改它都必須重新粘貼或重新選擇文件。

### 本地 HTTP 服務器（推薦）

本地 Web 服務器讓 RemixWarp 通過 URL 獲取您的擴展，因此更改後只需重新加載頁面。如果您安裝了 Python，您已經有了一個服務器：

```bash
cd path/to/your/extensions
python3 -m http.server 8080
```

那會在 `http://localhost:8080/` 提供當前文件夾。在該文件夾中放一個名為 `hello-world.js` 的文件，並在繼續之前確認您可以在瀏覽器中打開 [http://localhost:8080/hello-world.js](http://localhost:8080/hello-world.js)。

現在請使用**不是 8000** 的端口。端口 8000 很特殊：它是 RemixWarp 信任用於運行[非沙箱](/building-extensions/unsandboxed)的 URL 之一，這帶有我們還沒有準備好的額外責任。從沙箱開始。

稍後我們會介紹[一個專門的開發服務器](/building-extensions/better-development-server)，但從最原始的設置開始可以讓各個部分可見。

## 下一步

讓我們[編寫您的第一個擴展](/building-extensions/hello-world)。
