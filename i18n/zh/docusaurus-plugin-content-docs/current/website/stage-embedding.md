---
title: 舞台嵌入
sidebar_position: 3
slug: /website/stage-embedding
---

# 舞台嵌入

除了标准的 iframe [嵌入方式](/website/embedding)之外，RemixWarp 还支持通过专用的**纯舞台播放器**——`fullscreen.html` 来嵌入作品。这种方式将项目直接加载到干净的完整舞台视图中，不带任何编辑器界面，非常适合展示已完成的作品。

## 工作原理

舞台播放器通过 `project_url` 查询参数加载外部的 `.sb3` 项目文件：

```
https://remixwarp.pages.dev/fullscreen.html?project_url=你的_SB3_地址
```

项目文件（`.sb3`）必须托管在公开可访问的 URL 上，并且需要支持 [CORS](/website/cors)，以便播放器能够获取该文件。

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

`project_url` 可以指向任何公开托管的 `.sb3` 文件，包括上传到你自己服务器、CDN 或云存储的文件。

## 对比：舞台模式 vs. iframe 嵌入

| 特性 | 标准 iframe 嵌入 | 舞台模式 (`fullscreen.html`) |
|------|-----------------|------------------------------|
| 项目来源 | Scratch / RemixWarp 项目 ID | 任何托管的 `.sb3` 文件 URL |
| 需要公开分享的项目 | 是 | 否 |
| 编辑器界面 | 无 | 无 |
| 全屏背景 | 由参数控制 | 由舞台控制 |
| CORS 要求 | 否 | 是（SB3 所在 URL 需要） |
| 自托管项目 | 使用打包器 | 直接托管 `.sb3` 文件 |
| 最佳用途 | 快速分享公开项目 | 自定义作品集、游戏站点、离线演示 |

## URL 参数

舞台播放器支持以下查询参数：

| 参数 | 说明 | 示例 |
|------|------|------|
| `project_url` | **必填。** 要加载的 `.sb3` 文件的 URL。 | `?project_url=https://example.com/project.sb3` |
| `autoplay` | 加载后自动运行项目。 | `?project_url=...&autoplay` |
| `turbo` | 启用极速模式以获得最佳性能。 | `?project_url=...&turbo` |
| `fps` | 设置自定义帧率（例如 `60`）。 | `?project_url=...&fps=60` |
| `hqpen` | 启用高质量画笔渲染。 | `?project_url=...&hqpen` |
| `interpolate` | 启用运动插值，使动画更加流畅。 | `?project_url=...&interpolate` |
| `username` | 设置积木中使用的用户名。 | `?project_url=...&username=玩家` |

### 多参数完整示例

```
https://remixwarp.pages.dev/fullscreen.html?project_url=https://rw-vep.pages.dev/BV1Cu5m6kENy.sb3&autoplay&turbo&fps=60
```

## 托管你的 SB3 文件

要使用舞台嵌入，你需要将 `.sb3` 文件托管在可访问的位置。以下是常见方案：

### 方案一：支持 CORS 的云存储

将 `.sb3` 上传到支持 CORS 头的服务，例如 Cloudflare R2、AWS S3（需要配置 CORS）或 GitHub Pages。

**示例（使用自定义域名的 Cloudflare R2）：**
```
https://rw-vep.pages.dev/BV1Cu5m6kENy.sb3
```

### 方案二：自托管

将 `.sb3` 放在与嵌入页面相同的服务器上（同源），这样可以完全避免 CORS 问题。

```
https://你的网站.com/projects/我的游戏.sb3
```

### 方案三：从 02Engine Packager 导出

使用 [02Engine Packager](https://packager.02engine.org/) 导出打包的 HTML 文件。你可以从中提取 `.sb3` 文件，或直接托管打包好的 HTML。详见 [打包器嵌入](/packager/embedding)。

## 安全注意事项

- **CORS**：`.sb3` 文件的托管服务器必须返回正确的 `Access-Control-Allow-Origin` 头以支持跨域请求。否则播放器无法获取该文件。
- **内容安全策略（CSP）**：如果在 iframe 中嵌入舞台播放器，请配置你的 CSP 允许 `frame-src https://remixwarp.pages.dev`。
- **Sandbox**：使用 iframe 的 `sandbox` 属性进行深度防御：

```html
<iframe
  src="https://remixwarp.pages.dev/fullscreen.html?project_url=..."
  sandbox="allow-scripts allow-same-origin allow-fullscreen"
  allowfullscreen
></iframe>
```

## 响应式嵌入

将舞台播放器包裹在保持舞台宽高比的响应式容器中：

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

`75%` 的内边距创建了 4:3 的宽高比以匹配默认的 Scratch 舞台。如果你的项目使用了自定义舞台尺寸，可调整为 `56.25%` 以适配 16:9 宽屏。

## 常见问题排查

### 项目无法加载
- 确认 `project_url` 是 `.sb3` 文件的直接链接（而非下载页面）。
- 检查文件托管是否支持 CORS。可以使用同源 URL 进行测试。
- 打开浏览器控制台查看 CORS 或网络错误。

### 白屏 / 空白舞台
- 确保 `.sb3` 文件是有效的 Scratch 3.0 项目文件。
- 尝试直接在浏览器中下载该 URL 以确认可以访问。
- 检查浏览器控制台中是否有内容安全策略（CSP）错误。

## 另请参阅

- [标准嵌入](/website/embedding) — 按 Scratch 或 RemixWarp 项目 ID 嵌入项目
- [02Engine Packager](https://packager.02engine.org/) — 将项目打包为独立 HTML 文件
- [打包器嵌入](/packager/embedding) — 嵌入打包后的项目文件
- [CORS 指南](/website/cors) — 了解项目托管的 CORS 配置
- [URL 参数](/website/url-parameters) — 所有可用的 URL 参数
