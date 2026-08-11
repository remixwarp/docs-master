---
title: 編輯器集成
sidebar_position: 7
---

# 編輯器集成

RemixWarp 編輯器可以將當前項目直接交給打包器，因此您可以在一步之內從編輯到打包構建，而無需保存和重新上傳文件。在底層，這是編輯器和打包器之間的一次小型 `postMessage` 握手，本文檔為工具開發者記錄了它。

## 握手

1. 編輯器在 `https://packager.02engine.org/?import_from=<編輯器來源>` 打開打包器。
2. 打包器向編輯器回傳 `{ p4: { type: 'ready-for-import' } }`。
3. 編輯器回覆 `{ p4: { type: 'start-import' } }`，這樣打包器可以顯示加載狀態。
4. 編輯器導出項目併發送 `{ p4: { type: 'finish-import', data, name } }`，傳輸 SB3 `ArrayBuffer`。
5. 如果導出失敗，編輯器改為發送 `{ p4: { type: 'cancel-import' } }`。

每條消息都包裹在一個 `p4` 對象中。

## finish-import

```js
source.postMessage({
  p4: {
    type: 'finish-import',
    data: buffer,        // SB3 ArrayBuffer
    name: 'My Project.sb3'
  }
}, origin, [buffer]);    // buffer 被轉移，而不是複製
```

## 備註

- 編輯器只處理來源為 `https://packager.02engine.org` 的消息。
- SB3 用 `vm.saveProjectSb3('arraybuffer')` 生成。
- 文件名是當前項目標題加 `.sb3` 後綴。

## 另請參閱

- [打包器概覽](/packager/overview)
