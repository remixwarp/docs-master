---
title: renderer.createDrawable()
---

# renderer.createDrawable()

创建一个新的可绘制对象（drawable），并将其添加到指定图层组中的场景里。

## 语法

```javascript
renderer.createDrawable(group)
```

## 参数

### group
**类型：** `string`

要添加可绘制对象的图层组。常用值：
- `'background'` - 位于所有角色之后
- `'video'` - 摄像头/视频图层
- `'pen'` - 画笔图层
- `'sprite'` - 角色图层

## 返回值

**类型：** `number`

新创建的可绘制对象 ID。

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

## 图层组

图层组决定了渲染顺序：
1. `background` - 最先渲染（位于所有内容之后）
2. `video` - 视频/摄像头图层
3. `pen` - 画笔图层
4. `sprite` - 最后渲染（角色）

## 另请参阅

- [destroyDrawable()](./destroyDrawable.md) - 销毁可绘制对象
- [updateDrawableProperties()](./updateDrawableProperties.md) - 修改可绘制对象属性
- [setDrawableOrder()](./setDrawableOrder.md) - 更改可绘制对象的 z 轴顺序
