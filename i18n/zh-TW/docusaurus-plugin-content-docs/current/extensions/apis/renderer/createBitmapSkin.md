---
title: renderer.createBitmapSkin()
---

# renderer.createBitmapSkin()

根據圖像數據創建一個新的位圖皮膚。

## 語法

```javascript
renderer.createBitmapSkin(bitmapData, costumeResolution, rotationCenter)
```

## 參數

### bitmapData
**類型：** `ImageData | HTMLImageElement | HTMLCanvasElement | HTMLVideoElement`

皮膚使用的源圖像數據。

### costumeResolution  
**類型：** `number`（可選，默認值：`1`）

位圖的分辨率倍數。數值越高表示分辨率越高的造型。

### rotationCenter
**類型：** `Array<number>`（可選）

`[x, y]` 旋轉中心點。如果未提供，則使用圖像的中心。

## 返回值

**類型：** `number`

新創建的皮膚 ID。

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

## 另請參閱

- [updateBitmapSkin()](./updateBitmapSkin.md) - 更新已有的位圖皮膚
- [createSVGSkin()](./createSVGSkin.md) - 創建 SVG 皮膚
- [destroySkin()](./destroySkin.md) - 銷燬皮膚
