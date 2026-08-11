---
title: 擴展概覽
sidebar_position: 1
---

# 擴展概覽

擴展向積木區添加核心積木分類之外的額外積木。一個擴展可以添加一整套新樂器、通過藍牙驅動實體機器人、讀取網絡攝像頭，或將原始 JavaScript 注入您編譯的項目。加載後，它的積木作為積木區底部的一個新分類出現。

## 添加擴展

點擊編輯器左下角的**添加擴展**按鈕（積木區下方的圖標）。這會打開擴展庫。點擊任何擴展來加載它。它的積木會立即添加到您的項目中，並與項目一起保存，因此任何後來打開項目的人都會得到相同的積木。

一些擴展做的不僅是添加積木：

- **硬件擴展**（micro:bit、LEGO、Vernier 傳感器）會打開連接對話框，讓您在積木做任何事情之前通過藍牙配對設備。
- **攝像頭擴展**（視頻偵測、人臉感知）第一次運行時向您的瀏覽器請求網絡攝像頭權限。

## 內置與遠程擴展

RemixWarp 在庫中提供兩種擴展：

- **內置**擴展與編輯器捆綁，可離線即時加載。這些包括 RemixWarp 積木、補丁、音樂、畫筆、視頻偵測、文字朗讀、翻譯、Makey Makey 和硬件擴展。
- **遠程**擴展在您第一次加載時從 URL 下載，因此它們需要互聯網連接才能加載。人臉感知就是其中之一。庫還鏈接到 [extensions.bilup.org](https://extensions.bilup.org/) 的完整 RemixWarp 擴展畫廊，那裡託管著數百個社區擴展。

一些內置擴展也需要互聯網才能真正工作（不只是加載）：文字朗讀和翻譯每次使用都會調用在線服務，硬件擴展可能獲取固件或連接資源。

## 加載自定義擴展

如果擴展不在庫中，您可以自己從 URL、本地文件或粘貼的 JavaScript 源碼加載。打開擴展庫並選擇**自定義擴展**。詳情請參閱[自定義擴展](/extensions/custom-extension)，包括沙箱和非沙箱擴展之間的區別以及您會看到的安全提示。

## 與 Scratch 的兼容性

一些擴展被標記為與 Scratch 不兼容（RemixWarp 積木、補丁和大多數自定義擴展）。使用它們的項目無法在 scratch.mit.edu 上運行。庫在加載其中一個之前會警告您。來自 Scratch 本身的擴展（音樂、畫筆、視頻偵測、文字朗讀、翻譯、Makey Makey 以及 LEGO / micro:bit / Vernier 硬件擴展）保持與 Scratch 兼容。

## 編寫自己的擴展

如果您想構建擴展而不僅僅是使用，請從[構建擴展：簡介](/building-extensions/introduction)開始。

## 另請參閱

- [自定義擴展](/extensions/custom-extension)
- [RemixWarp 積木](/extensions/mistwarp-blocks)
- [補丁](/extensions/patching)
- [構建擴展：簡介](/building-extensions/introduction)
