---
title: renderer.getDrawableOrder()
---

# renderer.getDrawableOrder()

返回可繪製對象在繪製列表中的位置。

## 語法

```javascript
renderer.getDrawableOrder(drawableID)
```

## 參數

### drawableID
**類型：** `number`

可繪製對象的 ID。

## 返回值

**類型：** `number`

在繪製列表中的位置（絕對位置，不是相對於圖層組的）。

## 示例

```javascript
const position = renderer.getDrawableOrder(drawableId);
console.log(`Drawable is at position ${position}`);
```

## 另請參閱

- [setDrawableOrder()](./setDrawableOrder.md)
