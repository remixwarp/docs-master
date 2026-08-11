---
title: 更好的開發服務器
sidebar_position: 11
---

# 更好的開發服務器

[簡介](/building-extensions/introduction)中的 Python HTTP 服務器能用，但它有兩個粗糙的邊緣。本頁是可選的，但平滑它們可以消除擴展開發中的大部分摩擦。

## 兩個問題

1. **緩存。** `python3 -m http.server` 設置的緩存頭讓瀏覽器保留您的舊文件。編輯擴展後，您常常必須硬刷新（忽略緩存重新加載）才能看到更改。
2. **沙箱。** 任何不是從受信任來源提供的內容都會[沙箱](/building-extensions/sandbox)加載，這強制每個積木一幀的延遲。學習時這沒問題，但它會掩蓋您的積木發佈後的真實行為。

## 在端口 8000 上提供服務以非沙箱開發

`http://localhost:8000/` 是 RemixWarp 信任的來源之一，因此從那裡提供的擴展會自動以[非沙箱](/building-extensions/unsandboxed)方式加載，無需每次加載的提示。將您的靜態服務器指向 8000 端口並直接加載文件：

```bash
cd path/to/your/extensions
python3 -m http.server 8000
```

然後加載 `http://localhost:8000/your-extension.js`（或用 `?extension=http://localhost:8000/your-extension.js` 自動加載）。它必須恰好是 8000 端口上的 `localhost`；`127.0.0.1` 和 `0.0.0.0` 不受信任。

給擴展一個包含您名字的 ID，如 `yournamefetch`，這樣它不會與任何其他人的擴展 ID 衝突。

## 擺脫硬刷新

使用任何發送 no-cache 頭的靜態服務器，而不是裸的 Python 服務器。例如，安裝了 Node.js：

```bash
npx http-server -p 8000 -c-1
```

`-c-1` 禁用緩存，因此普通刷新總是獲取當前文件。任何等效的靜態服務器都可以；唯一重要的是它在 8000 端口上運行並且不緩存。

## 下一步

有了更快的循環，讓我們介紹[擴展可以使用的更多 API 和選項](/building-extensions/assorted-apis)。
