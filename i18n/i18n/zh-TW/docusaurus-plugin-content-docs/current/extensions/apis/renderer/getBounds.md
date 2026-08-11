---
title: renderer.getBounds()
---

# renderer.getBounds()

以 Scratch 座標獲取可繪製對象的緊緻包圍盒。

## 語法

```javascript
renderer.getBounds(drawableID)
```

## 參數

### drawableID
**類型：** `number`

可繪製對象的 ID。

## 返回值

**類型：** `object`

一個包含以下屬性的對象：
- `left`、`right`、`top`、`bottom`（Scratch 座標）
- `width`、`height`

## 示例

```javascript
const bounds = renderer.getBounds(drawableId);
console.log(`Left: ${bounds.left}, Top: ${bounds.top}`);
```

## 另請參閱

- [getBoundsForBubble()](./getBoundsForBubble.md)
