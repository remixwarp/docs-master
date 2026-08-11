---
title: renderer.createPenSkin()
---

# renderer.createPenSkin()

創建一個新的 PenSkin，它實現了 Scratch 的畫筆圖層。

## 語法

```javascript
renderer.createPenSkin()
```

## 參數

無。

## 返回值

**類型：** `number`

新的畫筆皮膚 ID。

## 示例

```javascript
const penSkinId = renderer.createPenSkin();
// Pen skins are automatically managed by the renderer for pen operations
```

## 另請參閱

- [createBitmapSkin()](./createBitmapSkin.md)
- [createSVGSkin()](./createSVGSkin.md)
