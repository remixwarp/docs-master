---
title: renderer.draw()
---

# renderer.draw()

手动触发舞台的一次渲染。

## 语法

```javascript
renderer.draw()
```

## 参数

无。

## 返回值

**类型：** `void`

## 说明

渲染器通常会自动处理绘制。除非你在进行自定义的离屏渲染，或需要在更改后立即强制更新，否则很少需要手动调用此方法。

## 另请参阅

- [requestSnapshot()](./requestSnapshot.md)
