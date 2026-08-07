---
title: renderer.createSVGSkin()
---

# renderer.createSVGSkin()

根据 SVG 标记创建一个新的 SVG 皮肤。

## 语法

```javascript
renderer.createSVGSkin(svgData, rotationCenter)
```

## 参数

### svgData
**类型：** `string`

以字符串形式表示的 SVG 标记。

### rotationCenter
**类型：** `Array<number>`（可选）  

`[x, y]` 旋转中心点。如果未提供，则使用 SVG 的中心。

## 返回值

**类型：** `number`

新创建的皮肤 ID。

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

## 说明

- SVG 皮肤是异步加载的 - 请参阅 [SVG 加载](../../concepts/svg-loading.md)
- SVG 内容应包含正确的 xmlns 属性
- 旋转中心坐标相对于 SVG 的 viewBox

## 另请参阅

- [updateSVGSkin()](./updateSVGSkin.md) - 更新已有的 SVG 皮肤
- [createBitmapSkin()](./createBitmapSkin.md) - 创建位图皮肤
- [destroySkin()](./destroySkin.md) - 销毁皮肤
- [SVG 加载模式](../../concepts/svg-loading.md) - 处理异步 SVG 加载
