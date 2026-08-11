---
title: 嵌入
sidebar_position: 4
---

# 嵌入

您可以使用標準 `<iframe>` 將 RemixWarp 項目嵌入到任何網站中。嵌入只顯示舞臺和控件，沒有編輯器環繞。

```html
<iframe
  src="https://remixwarp.pages.dev/414716080/embed"
  width="482"
  height="412"
  frameborder="0"
  scrolling="no"
  allowfullscreen
></iframe>
```

將 `414716080` 替換為您的項目 ID。您可以選擇任意寬度和高度；播放器會自動調整大小。`482x412` 的 iframe 以不變形的 `480x360` 渲染舞臺（額外 52 像素為控制欄留出空間）。嵌入具有透明背景，並在瀏覽器允許時提供全屏按鈕。

## Scratch 和 RemixWarp 項目

URL 中的 ID 可以是兩種項目之一：

- **Scratch 項目 ID**（純數字，如 `414716080`）嵌入在 Scratch 上共享的項目。
- **RemixWarp 社區項目 ID**（如 `p1784079025833421000VYnQRa`）嵌入在 RemixWarp 社區網站上共享的項目。這是項目頁面 URL 中的 ID，`https://remixwarp.pages.dev/project/p1784079025833421000VYnQRa`。

```html
<iframe src="https://remixwarp.pages.dev/p1784079025833421000VYnQRa/embed"></iframe>
```

兩者使用相同的 `/embed` 路徑、參數和下文描述的 postMessage API。

::::note
未共享的項目無法嵌入。請先分享項目，或者使用[RemixWarp 打包器](/packager/overview)打包後[嵌入打包文件](/packager/embedding)。請參閱[未共享項目](/advanced/unshared-projects)。
::::

## URL 參數

所有[標準 URL 參數](/advanced/url-parameters)都適用於嵌入，另外還有幾個僅適用於嵌入的參數。

| 參數 | 作用 |
|-----------|--------------|
| `autoplay` | 項目加載後自動點擊綠旗。 |
| `settings-button` | 在嵌入中添加高級設置按鈕。 |
| `fullscreen-background` | 設置全屏背景顏色。將 `#` 轉義為 `%23`。 |
| `addons` | 啟用特定插件（見下文）。 |

```html
<iframe src="https://remixwarp.pages.dev/15832807/embed?autoplay&settings-button"></iframe>
```

聲音積木可能直到用戶與項目交互（例如點擊）後才會播放。這是瀏覽器限制，不是 RemixWarp 可以繞過的，因此 autoplay 無法在加載時強制播放音頻。

### 嵌入中的插件

嵌入默認不啟用任何插件。`addons` 參數接受逗號分隔的插件 ID 列表：

```
https://remixwarp.pages.dev/15832807/embed?addons=pause,gamepad,mute-project
```

嵌入中有用的插件包括：

- `pause`（暫停按鈕）
- `mute-project`（靜音播放器）
- `remove-curved-stage-border`
- `drag-drop`（文件拖放）
- `gamepad`（手柄支持）
- `clones`（克隆計數器）

隻影響編輯器的插件在此處沒有效果。

## 響應式嵌入

要讓嵌入隨容器縮放，請將其包裹在帶內邊距的盒子中：

```html
<div style="position: relative; padding-bottom: 75%; height: 0;">
  <iframe
    src="https://remixwarp.pages.dev/123456789/embed"
    style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"
    frameborder="0"
    allowfullscreen
  ></iframe>
</div>
```

`75%` 的內邊距提供匹配默認舞臺的 4:3 盒子。如果使用[自定義舞臺大小](/advanced/custom-stage-size)，請調整它。

## 運行時通過 postMessage 加載項目

宿主頁面可以不把項目 ID 放在 URL 中，而是在嵌入加載後將 SB3 發送給它。這對於自定義加載器或項目來自項目 ID 之外的地方時非常有用。

發送 `LOAD_SB3` 消息：

```js
const iframe = document.getElementById('mistwarp-embed');
iframe.contentWindow.postMessage({
  type: 'LOAD_SB3',
  data: 'https://example.com/project.sb3', // URL 字符串、ArrayBuffer 或 Uint8Array
  title: '可選標題'
}, '*');
```

`data` 可以是：

- 嵌入將獲取的 **URL 字符串**（必須支持 [CORS](/advanced/cors)），
- 原始 SB3 字節的 **ArrayBuffer**，或
- 原始 SB3 字節的 **Uint8Array**。

嵌入會回覆 `LOAD_SB3_RESPONSE` 消息：

```js
window.addEventListener('message', (event) => {
  const msg = event.data;
  if (msg && msg.type === 'LOAD_SB3_RESPONSE') {
    // msg.status:  'success' 或 'error'
    // msg.message: 人類可讀的詳細信息
    // msg.title:   您傳入的標題
    // msg.timestamp: 毫秒
    console.log(msg.status, msg.message);
  }
});
```

成功時 VM 會重啟並加載新項目。如果希望加載後自動啟動，請在嵌入 URL 中添加 `autoplay`。

出於安全考慮，嵌入只接受來自可信來源的 `LOAD_SB3`：同源頁面、`https://` 父頁面、用於本地測試的 `file://`，以及本地開發端口 `3000`、`8080` 和 `8601`。來自其他來源的消息會被忽略。

## 安全

如果您根據用戶提供的數據構建嵌入鏈接，請對輸入進行清理。能夠注入任意 URL 參數的用戶可以改變嵌入的行為。您還可以添加 iframe `sandbox` 屬性進行縱深防禦：

```html
<iframe
  src="https://remixwarp.pages.dev/123456789/embed"
  sandbox="allow-scripts allow-same-origin allow-fullscreen"
></iframe>
```

## 當您需要更多控制

如果需要對加載屏幕、控件和單文件打包進行控制，請使用[RemixWarp 打包器](/packager/overview)。打包項目也可以[嵌入](/packager/embedding)。

## 另請參閱

- [URL 參數](/advanced/url-parameters)
- [未共享項目](/advanced/unshared-projects)
- [打包器：嵌入](/packager/embedding)
- [CORS](/advanced/cors)
