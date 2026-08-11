---
title: renderer.getCurrentSkinSize()
---

# renderer.getCurrentSkinSize()

获取当前分配给某个可绘制对象的皮肤的大小。

## 语法

```javascript
renderer.getCurrentSkinSize(drawableID)
```

## 参数

### drawableID
**类型：** `number`

可绘制对象的 ID。

## 返回值

**类型：** `Array<number>`

一个表示皮肤大小的数组 `[width, height]`。

## 示例

```javascript
const [width, height] = renderer.getCurrentSkinSize(drawableId);
```

## 另请参阅

- [getSkinSize()](./getSkinSize.md)
