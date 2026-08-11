---
title: renderer.createDrawable()
---

# renderer.createDrawable()

創建一個新的可繪製對象（drawable），並將其添加到指定圖層組中的場景裡。

## 語法

```javascript
renderer.createDrawable(group)
```

## 參數

### group
**類型：** `string`

要添加可繪製對象的圖層組。常用值：
- `'background'` - 位於所有角色之後
- `'video'` - 攝像頭/視頻圖層
- `'pen'` - 畫筆圖層
- `'sprite'` - 角色圖層

## 返回值

**類型：** `number`

新創建的可繪製對象 ID。

## 示例

```javascript
class CustomGraphicsExtension {
  constructor(runtime) {
    this.runtime = runtime;
    this.drawables = new Map();
  }
  
  createCustomDrawable(args, util) {
    const renderer = util.runtime.renderer;
    
    // Create drawable in sprite layer
    const drawableId = renderer.createDrawable('sprite');
    
    // Set initial properties  
    renderer.updateDrawableProperties(drawableId, {
      position: [0, 0, 0],
      visible: true,
      scale: [100, 100]
    });
    
    // Store reference
    this.drawables.set(args.NAME, drawableId);
    
    return drawableId;
  }
}
```

## 圖層組

圖層組決定了渲染順序：
1. `background` - 最先渲染（位於所有內容之後）
2. `video` - 視頻/攝像頭圖層
3. `pen` - 畫筆圖層
4. `sprite` - 最後渲染（角色）

## 另請參閱

- [destroyDrawable()](./destroyDrawable.md) - 銷燬可繪製對象
- [updateDrawableProperties()](./updateDrawableProperties.md) - 修改可繪製對象屬性
- [setDrawableOrder()](./setDrawableOrder.md) - 更改可繪製對象的 z 軸順序
