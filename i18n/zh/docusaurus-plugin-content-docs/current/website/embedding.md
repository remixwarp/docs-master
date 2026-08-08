---
slug: /embedding
hide_table_of_contents: true
---

# 嵌入

RemixWarp 项目可以使用标准的 iframe 进行嵌入：

```html
<iframe src="https://remixwarp.pages.dev/414716080/embed" width="482" height="412" frameborder="0" scrolling="no" allowfullscreen></iframe>
```

将 `414716080` 替换为你的项目 ID。你可以更改 iframe 的宽度和高度，播放器会自动调整大小以适应（482x412 将使舞台以未失真的 480x360 渲染）。

嵌入内容具有透明背景，并且在浏览器允许的情况下有全屏按钮。

## 未分享的项目无法嵌入 {#unshared-projects}

未分享的项目[无法在嵌入中显示](unshared-projects)。请确保你嵌入的项目是已分享的，或改用 [02Engine Packager](https://packager.02engine.org/)。

## URL 参数 {#url-parameters}

所有[标准 URL 参数](url-parameters.md)均可使用。你可以用它们来控制用户名和其他内容。

还有一些仅在嵌入中可用的特殊参数：

### 自动播放 {#autoplay}

嵌入支持 `autoplay` 参数，项目加载时会自动点击绿旗。例如：

```
https://remixwarp.pages.dev/414716080/embed?autoplay
```

请注意，声音积木可能要到用户与项目交互（例如点击）之后才能正常工作。这是浏览器的限制，RemixWarp 无法绕过。

### 设置按钮 {#settings-button}

你可以通过 `settings-button` 参数在嵌入中启用设置按钮，它会打开一个类似于网站和编辑器中"高级设置"菜单的菜单。例如：

```
https://remixwarp.pages.dev/414716080/embed?settings-button
```

### 全屏背景颜色 {#fullscreen-background}

在全屏模式之外，嵌入内容是透明的，因此你可以通过设置父元素的样式来更改背景颜色。

在全屏模式下，嵌入内容会根据用户的计算机是否配置了深色模式，使用白色或接近黑色的颜色。

要覆盖此行为，请将 `fullscreen-background` 参数设置为 CSS 颜色值，例如 `black` 或 `rgb(50,90,100)`。例如：

```
https://remixwarp.pages.dev/414716080/embed?fullscreen-background=black
```

你也可以使用十六进制颜色，只需将 `#` 用百分号编码转义：`%23abc123`。

### 插件 {#addons}

默认情况下，嵌入没有启用任何插件。可以通过 `addons` 参数来覆盖，它是一个逗号分隔的插件 ID 列表。例如：

```
https://remixwarp.pages.dev/414716080/embed?addons=pause,mute-project
```

有用的插件及其 ID：
 - "暂停按钮"是 `pause`
 - "静音项目播放器模式"是 `mute-project`
 - "移除弯曲舞台边框"是 `remove-curved-stage-border`
 - "文件拖放"是 `drag-drop`
 - "游戏手柄支持"是 `gamepad`
 - "反转项目控件顺序"是 `editor-buttons-reverse-order`
 - "克隆计数器"是 `clones`

其他插件在嵌入中不起作用。

## 安全注意事项 {#security}

如果你使用用户提供的信息来生成嵌入链接，应清理任何参数，以确保用户无法提供可能导致意外行为的任意 URL 参数。

## 需要更多控制？ {#packager}

使用 [02Engine Packager](https://packager.02engine.org/) 来获得对加载画面和 UI 的更多控制。你也可以非常轻松地[嵌入打包器的输出](/packager/embedding)。

---

## 通过舞台模式嵌入 {#stage-mode}

你还可以使用 RemixWarp 的全屏舞台模式来嵌入项目，该模式将项目直接加载到舞台上，无需编辑器 UI。这非常适合以干净、无干扰的播放器展示项目。

<div style="background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); border-radius: 12px; padding: 24px; margin: 24px 0; color: white;">
  <h3 style="margin-top: 0; color: white;">🎬 舞台嵌入指南</h3>
  <p style="opacity: 0.9; margin-bottom: 16px;">了解如何使用 fullscreen.html 舞台播放器嵌入项目——将外部 SB3 文件直接加载到独立播放器视图中。</p>
  <a href="/website/stage-embedding" style="display: inline-block; background: white; color: #667eea; padding: 10px 24px; border-radius: 8px; text-decoration: none; font-weight: 600;">阅读舞台嵌入指南 →</a>
</div>

## 捐赠 {#donations}

如果你在商业网站中使用 RemixWarp 嵌入，请考虑[捐赠](/donate)以支持托管和上游项目。❤️

## 许可证 {#license}

TurboWarp 采用 [GPLv3.0](https://www.gnu.org/licenses/gpl-3.0.html) 许可证。我们认为，GPLv3.0 作品的 `<iframe>` 不会创建 GPLv3.0 下的衍生作品，而是创建了"聚合作品"，其要求与衍生作品不同。然而，我们不是律师，这也不是法律建议。如果这对你很重要，请咨询律师。
