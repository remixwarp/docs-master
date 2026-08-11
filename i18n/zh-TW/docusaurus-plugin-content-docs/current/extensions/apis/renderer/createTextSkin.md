---
title: renderer.createTextSkin()
---

# renderer.createTextSkin()

使用文本氣泡創建器（如"說"或"思考"氣泡）創建一個新的 SVG 皮膚。

## 語法

```javascript
renderer.createTextSkin(type, text, pointsLeft)
```

## 參數

### type
**類型：** `string`

氣泡類型：`'say'` 或 `'think'`。

### text
**類型：** `string`

氣泡的文本內容。

### pointsLeft
**類型：** `boolean`

如果為 `true`，氣泡尾部指向左側；如果為 `false`，則指向右側。

## 返回值

**類型：** `number`

新皮膚的 ID。

## 示例

```javascript
const skinId = renderer.createTextSkin('say', 'Hello World!', true);
```

## 另請參閱

- [updateTextSkin()](./updateTextSkin.md)
- [createSVGSkin()](./createSVGSkin.md)
