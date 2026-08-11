---
title: renderer.destroyDrawable()
---

# renderer.destroyDrawable()

銷燬一個可繪製對象，並將其從場景中移除。釋放關聯的資源。

## 語法

```javascript
renderer.destroyDrawable(drawableID, group)
```

## 參數

### drawableID
**類型：** `number`

要銷燬的可繪製對象 ID。

### group
**類型：** `string`

該可繪製對象所屬的圖層組（`'background'`、`'video'`、`'pen'` 或 `'sprite'`）。

## 返回值

**類型：** `void`

## 示例

```javascript
class DrawableManagerExtension {
  removeDrawable(args) {
    const renderer = this.runtime.renderer;
    const drawableId = this.drawables.get(args.NAME);
    
    if (drawableId) {
      renderer.destroyDrawable(drawableId, 'sprite');
      this.drawables.delete(args.NAME);
    }
  }
}
```

## 另請參閱

- [createDrawable()](./createDrawable.md)
- [updateDrawableProperties()](./updateDrawableProperties.md)
