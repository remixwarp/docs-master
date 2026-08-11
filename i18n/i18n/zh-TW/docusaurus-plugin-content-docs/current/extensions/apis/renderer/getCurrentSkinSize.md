---
title: renderer.getCurrentSkinSize()
---

# renderer.getCurrentSkinSize()

獲取當前分配給某個可繪製對象的皮膚的大小。

## 語法

```javascript
renderer.getCurrentSkinSize(drawableID)
```

## 參數

### drawableID
**類型：** `number`

可繪製對象的 ID。

## 返回值

**類型：** `Array<number>`

一個表示皮膚大小的數組 `[width, height]`。

## 示例

```javascript
const [width, height] = renderer.getCurrentSkinSize(drawableId);
```

## 另請參閱

- [getSkinSize()](./getSkinSize.md)
