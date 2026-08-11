---
title: renderer.createBitmapSkin()
---

# renderer.createBitmapSkin()

根据图像数据创建一个新的位图皮肤。

## 语法

```javascript
renderer.createBitmapSkin(bitmapData, costumeResolution, rotationCenter)
```

## 参数

### bitmapData
**类型：** `ImageData | HTMLImageElement | HTMLCanvasElement | HTMLVideoElement`

皮肤使用的源图像数据。

### costumeResolution  
**类型：** `number`（可选，默认值：`1`）

位图的分辨率倍数。数值越高表示分辨率越高的造型。

### rotationCenter
**类型：** `Array<number>`（可选）

`[x, y]` 旋转中心点。如果未提供，则使用图像的中心。

## 返回值

**类型：** `number`

新创建的皮肤 ID。

## 示例

```javascript
class MyExtension {
  async loadBitmapSkin(args, util) {
    const renderer = util.runtime.renderer;
    
    // Load image from URL
    const img = new Image();
    img.crossOrigin = 'anonymous';
    img.src = args.URL;
    await img.decode();
    
    // Create bitmap skin
    const skinId = renderer.createBitmapSkin(img, 1);
    
    return skinId;
  }
}
```

## 另请参阅

- [updateBitmapSkin()](./updateBitmapSkin.md) - 更新已有的位图皮肤
- [createSVGSkin()](./createSVGSkin.md) - 创建 SVG 皮肤
- [destroySkin()](./destroySkin.md) - 销毁皮肤
