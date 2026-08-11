---
title: renderer.createSVGSkin()
---

# renderer.createSVGSkin()

根據 SVG 標記創建一個新的 SVG 皮膚。

## 語法

```javascript
renderer.createSVGSkin(svgData, rotationCenter)
```

## 參數

### svgData
**類型：** `string`

以字符串形式表示的 SVG 標記。

### rotationCenter
**類型：** `Array<number>`（可選）  

`[x, y]` 旋轉中心點。如果未提供，則使用 SVG 的中心。

## 返回值

**類型：** `number`

新創建的皮膚 ID。

## 示例

```javascript
class SVGExtension {
  createCircleSkin(args, util) {
    const renderer = util.runtime.renderer;
    const color = args.COLOR || '#ff0000';
    const size = args.SIZE || 100;
    
    const svgData = `
      <svg width="${size}" height="${size}" xmlns="http://www.w3.org/2000/svg">
        <circle cx="${size/2}" cy="${size/2}" r="${size/2}" fill="${color}" />
      </svg>
    `;
    
    const skinId = renderer.createSVGSkin(svgData);
    return skinId;
  }
}
```

## 說明

- SVG 皮膚是異步加載的 - 請參閱 [SVG 加載](../../concepts/svg-loading.md)
- SVG 內容應包含正確的 xmlns 屬性
- 旋轉中心座標相對於 SVG 的 viewBox

## 另請參閱

- [updateSVGSkin()](./updateSVGSkin.md) - 更新已有的 SVG 皮膚
- [createBitmapSkin()](./createBitmapSkin.md) - 創建位圖皮膚
- [destroySkin()](./destroySkin.md) - 銷燬皮膚
- [SVG 加載模式](../../concepts/svg-loading.md) - 處理異步 SVG 加載
