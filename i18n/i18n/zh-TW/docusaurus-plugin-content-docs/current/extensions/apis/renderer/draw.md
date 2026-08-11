---
title: renderer.draw()
---

# renderer.draw()

手動觸發舞臺的一次渲染。

## 語法

```javascript
renderer.draw()
```

## 參數

無。

## 返回值

**類型：** `void`

## 說明

渲染器通常會自動處理繪製。除非你在進行自定義的離屏渲染，或需要在更改後立即強制更新，否則很少需要手動調用此方法。

## 另請參閱

- [requestSnapshot()](./requestSnapshot.md)
