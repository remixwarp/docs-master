---
title: 嵌入
sidebar_position: 2
slug: /packager/embedding
---

# 嵌入打包項目

::::info
本頁講述嵌入[02Engine Packager](/packager/overview)的輸出。如果您只是想嵌入共享項目而不打包它，請參閱[嵌入](/website/embedding)。
::::

當您將項目打包為 HTML 時，您會得到一個自包含的文件，可以自己託管，並用 `<iframe>` 放入任何頁面：

```html
<iframe
  src="path_to_project.html"
  width="480"
  height="360"
  allowtransparency="true"
  frameborder="0"
  scrolling="no"
  allowfullscreen
></iframe>
```

`src` 取決於您如何導出：

- **純 HTML**：單個 HTML 文件的路徑。
- **Zip**：解壓後的 zip 中 `index.html` 的路徑。

如果您在打包器中啟用了屏幕控件（綠旗、停止、全屏），請在 `height` 上加上 `48`，這樣控制欄不會縮小舞臺。

因為打包項目只是您託管的文件，嵌入它對未在 Scratch 上共享的項目也有效，與[託管嵌入播放器](/website/embedding)不同。

## 另請參閱

- [打包器概覽](/packager/overview)
- [嵌入共享項目](/website/embedding)
