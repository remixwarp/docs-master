---
title: 舞臺嵌入
sidebar_position: 3
slug: /website/stage-embedding
---

# 舞臺嵌入

除了標準的 iframe [嵌入方式](/website/embedding)之外，RemixWarp 還支持通過專用的**純舞臺播放器**——`fullscreen.html` 來嵌入作品。這種方式將項目直接加載到乾淨的完整舞臺視圖中，不帶任何編輯器界面，非常適合展示已完成的作品。

## 工作原理

舞臺播放器通過 `project_url` 查詢參數加載外部的 `.sb3` 項目文件：

```
https://remixwarp.pages.dev/fullscreen.html?project_url=你的_SB3_地址
```

項目文件（`.sb3`）必須託管在公開可訪問的 URL 上，並且需要支持 [CORS](/website/cors)，以便播放器能夠獲取該文件。

## 基本用法

```html
<iframe
  src="https://remixwarp.pages.dev/fullscreen.html?project_url=https://rw-vep.pages.dev/BV1Cu5m6kENy.sb3"
  width="960"
  height="720"
  frameborder="0"
  scrolling="no"
  allowfullscreen
></iframe>
```

`project_url` 可以指向任何公開託管的 `.sb3` 文件，包括上傳到你自己服務器、CDN 或雲存儲的文件。

## 對比：舞臺模式 vs. iframe 嵌入

| 特性 | 標準 iframe 嵌入 | 舞臺模式 (`fullscreen.html`) |
|------|-----------------|------------------------------|
| 項目來源 | Scratch / RemixWarp 項目 ID | 任何託管的 `.sb3` 文件 URL |
| 需要公開分享的項目 | 是 | 否 |
| 編輯器界面 | 無 | 無 |
| 全屏背景 | 由參數控制 | 由舞臺控制 |
| CORS 要求 | 否 | 是（SB3 所在 URL 需要） |
| 自託管項目 | 使用打包器 | 直接託管 `.sb3` 文件 |
| 最佳用途 | 快速分享公開項目 | 自定義作品集、遊戲站點、離線演示 |

## URL 參數

舞臺播放器支持以下查詢參數：

| 參數 | 說明 | 示例 |
|------|------|------|
| `project_url` | **必填。** 要加載的 `.sb3` 文件的 URL。 | `?project_url=https://example.com/project.sb3` |
| `autoplay` | 加載後自動運行項目。 | `?project_url=...&autoplay` |
| `turbo` | 啟用極速模式以獲得最佳性能。 | `?project_url=...&turbo` |
| `fps` | 設置自定義幀率（例如 `60`）。 | `?project_url=...&fps=60` |
| `hqpen` | 啟用高質量畫筆渲染。 | `?project_url=...&hqpen` |
| `interpolate` | 啟用運動插值，使動畫更加流暢。 | `?project_url=...&interpolate` |
| `username` | 設置積木中使用的用戶名。 | `?project_url=...&username=玩家` |

### 多參數完整示例

```
https://remixwarp.pages.dev/fullscreen.html?project_url=https://rw-vep.pages.dev/BV1Cu5m6kENy.sb3&autoplay&turbo&fps=60
```

## 託管你的 SB3 文件

要使用舞臺嵌入，你需要將 `.sb3` 文件託管在可訪問的位置。以下是常見方案：

### 方案一：支持 CORS 的雲存儲

將 `.sb3` 上傳到支持 CORS 頭的服務，例如 Cloudflare R2、AWS S3（需要配置 CORS）或 GitHub Pages。

**示例（使用自定義域名的 Cloudflare R2）：**
```
https://rw-vep.pages.dev/BV1Cu5m6kENy.sb3
```

### 方案二：自託管

將 `.sb3` 放在與嵌入頁面相同的服務器上（同源），這樣可以完全避免 CORS 問題。

```
https://你的網站.com/projects/我的遊戲.sb3
```

### 方案三：從 02Engine Packager 導出

使用 [02Engine Packager](https://packager.02engine.org/) 導出打包的 HTML 文件。你可以從中提取 `.sb3` 文件，或直接託管打包好的 HTML。詳見 [打包器嵌入](/packager/embedding)。

## 安全注意事項

- **CORS**：`.sb3` 文件的託管服務器必須返回正確的 `Access-Control-Allow-Origin` 頭以支持跨域請求。否則播放器無法獲取該文件。
- **內容安全策略（CSP）**：如果在 iframe 中嵌入舞臺播放器，請配置你的 CSP 允許 `frame-src https://remixwarp.pages.dev`。
- **Sandbox**：使用 iframe 的 `sandbox` 屬性進行深度防禦：

```html
<iframe
  src="https://remixwarp.pages.dev/fullscreen.html?project_url=..."
  sandbox="allow-scripts allow-same-origin allow-fullscreen"
  allowfullscreen
></iframe>
```

## 響應式嵌入

將舞臺播放器包裹在保持舞臺寬高比的響應式容器中：

```html
<div style="position: relative; padding-bottom: 75%; height: 0;">
  <iframe
    src="https://remixwarp.pages.dev/fullscreen.html?project_url=https://example.com/project.sb3"
    style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"
    frameborder="0"
    allowfullscreen
  ></iframe>
</div>
```

`75%` 的內邊距創建了 4:3 的寬高比以匹配默認的 Scratch 舞臺。如果你的項目使用了自定義舞臺尺寸，可調整為 `56.25%` 以適配 16:9 寬屏。

## 常見問題排查

### 項目無法加載
- 確認 `project_url` 是 `.sb3` 文件的直接鏈接（而非下載頁面）。
- 檢查文件託管是否支持 CORS。可以使用同源 URL 進行測試。
- 打開瀏覽器控制台查看 CORS 或網絡錯誤。

### 白屏 / 空白舞臺
- 確保 `.sb3` 文件是有效的 Scratch 3.0 項目文件。
- 嘗試直接在瀏覽器中下載該 URL 以確認可以訪問。
- 檢查瀏覽器控制台中是否有內容安全策略（CSP）錯誤。

## 另請參閱

- [標準嵌入](/website/embedding) — 按 Scratch 或 RemixWarp 項目 ID 嵌入項目
- [02Engine Packager](https://packager.02engine.org/) — 將項目打包為獨立 HTML 文件
- [打包器嵌入](/packager/embedding) — 嵌入打包後的項目文件
- [CORS 指南](/website/cors) — 瞭解項目託管的 CORS 配置
- [URL 參數](/website/url-parameters) — 所有可用的 URL 參數
