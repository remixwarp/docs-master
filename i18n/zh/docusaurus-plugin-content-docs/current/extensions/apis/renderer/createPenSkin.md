---
title: renderer.createPenSkin()
---

# renderer.createPenSkin()

创建一个新的 PenSkin，它实现了 Scratch 的画笔图层。

## 语法

```javascript
renderer.createPenSkin()
```

## 参数

无。

## 返回值

**类型：** `number`

新的画笔皮肤 ID。

## 示例

```javascript
const penSkinId = renderer.createPenSkin();
// Pen skins are automatically managed by the renderer for pen operations
```

## 另请参阅

- [createBitmapSkin()](./createBitmapSkin.md)
- [createSVGSkin()](./createSVGSkin.md)
