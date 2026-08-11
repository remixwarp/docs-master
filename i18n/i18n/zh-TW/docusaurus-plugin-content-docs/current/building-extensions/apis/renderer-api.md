---
title: 渲染器 API
sidebar_position: 5
---

# 渲染器 API

渲染器（scratch-render）用 WebGL 繪製舞臺。[非沙箱擴展](/building-extensions/unsandboxed)在 `Scratch.renderer` 訪問它（等價於 `util.runtime.renderer`）。

大多數擴展從不接觸渲染器；角色會自動繪製。只有當您想在舞臺上繪製自己的圖形時才需要它。模型有兩層：

- **皮膚**持有紋理（位圖、SVG、畫筆畫布或文本）。
- **可繪製對象**是引用皮膚的有位置實例。您給可繪製對象一個皮膚，然後設置它的位置、縮放、效果和圖層。

```js
myBlock(args, util) {
  const renderer = util.runtime.renderer;

  const skinId = renderer.createBitmapSkin(imageData, 1);
  const drawableId = renderer.createDrawable('pen'); // 一個圖層組
  renderer.updateDrawableSkinId(drawableId, skinId);
  renderer.updateDrawableProperties(drawableId, {
    position: [0, 0],
    scale: [100, 100],
    visible: true
  });
}
```

這些是內部 API。它們可能隨 RemixWarp 版本而更改，因此請保護您的代碼並清理您創建的皮膚和可繪製對象。

## 皮膚

| 方法 | 描述 |
|:--|:--|
| `createBitmapSkin(bitmapData, resolution, rotationCenter?)` | 從 `ImageData`、畫布或圖像創建皮膚。`resolution` 通常是 `1` 或 `2`。返回皮膚 id。 |
| `createSVGSkin(svgData, rotationCenter?)` | 從 SVG 字符串創建皮膚。返回皮膚 id。 |
| `createPenSkin()` | 您用畫筆方法在其上繪製的空皮膚。返回皮膚 id。 |
| `createTextSkin(type, text, pointsLeft)` | 對話/思考氣泡皮膚。 |
| `updateBitmapSkin(skinId, imgData, resolution, rotationCenter?)` | 替換位圖皮膚的內容。 |
| `updateSVGSkin(skinId, svgData, rotationCenter?)` | 替換 SVG 皮膚的內容。 |
| `destroySkin(skinId)` | 釋放皮膚。用完時執行此操作。 |
| `getSkinSize(skinId)` | 皮膚的 `[寬度, 高度]`。 |
| `getSkinRotationCenter(skinId)` | `[x, y]` 旋轉中心。 |

## 可繪製對象

| 方法 | 描述 |
|:--|:--|
| `createDrawable(group)` | 在圖層組中創建可繪製對象（例如 `'pen'`）。返回可繪製對象 id。 |
| `destroyDrawable(drawableId, group)` | 移除可繪製對象。 |
| `updateDrawableSkinId(drawableId, skinId)` | 將可繪製對象指向皮膚。 |
| `updateDrawableProperties(drawableId, properties)` | 設置 `position` `[x,y]`、`direction`、`scale` `[sx,sy]`、`visible`、`ghost` 和其他效果，以及 `skinId`。 |
| `getCurrentSkinSize(drawableId)` | 可繪製對象當前皮膚的 `[寬度, 高度]`。 |
| `getBounds(drawableId)` | 舞臺座標中的緊密邊界框。 |
| `getDrawableOrder(drawableId)` | 可繪製對象在其組內的索引。 |
| `setDrawableOrder(drawableId, order, group, isRelative?, min?)` | 重新排序可繪製對象（更改分層）。 |

## 畫筆繪製

只適用於用 `createPenSkin()` 製作的皮膚。

| 方法 | 描述 |
|:--|:--|
| `penClear(penSkinId)` | 擦除畫筆層。 |
| `penPoint(penSkinId, penAttributes, x, y)` | 繪製一個點。 |
| `penLine(penSkinId, penAttributes, x0, y0, x1, y1)` | 繪製一條線。`penAttributes` 是 `{ color4f: [r,g,b,a], diameter }`。 |

## 碰撞

| 方法 | 描述 |
|:--|:--|
| `isTouchingColor(drawableId, color3b, mask3b?)` | 可繪製對象是否與顏色重疊。`color3b` 是 `[r,g,b]`（0 到 255）。 |
| `isTouchingDrawables(drawableId, candidateIds?)` | 可繪製對象是否與任何給定可繪製對象重疊。 |

## 舞臺與輸出

| 方法 | 描述 |
|:--|:--|
| `draw()` | 立即渲染一幀。 |
| `requestSnapshot(callback)` | 捕獲畫布；回調接收一個數據 URL。 |
| `setBackgroundColor(r, g, b, a?)` | 舞臺背景顏色。分量是 0 到 1。 |
| `resize(pixelsWide, pixelsTall)` | 設置畫布的物理像素大小。 |
| `setStageSize(xLeft, xRight, yBottom, yTop)` | 設置邏輯舞臺邊界。 |
| `renderer.canvas` | `<canvas>` 元素。 |

## 座標

舞臺座標與 Scratch 匹配：`(0, 0)` 是中心，x 向右增加，y 向上增加。在默認舞臺上 x 從 -240 到 240，y 從 -180 到 180，但[舞臺大小可以自定義](/advanced/custom-stage-size)，因此請讀取 `runtime.stageWidth` / `runtime.stageHeight`，而不是假設。

## 另請參閱

- [VM API](/building-extensions/apis/vm-api)
- [Scratch 對象 API](/building-extensions/apis/scratch-api)
