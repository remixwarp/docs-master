---
title: 保持兼容性
sidebar_position: 8
---

# 保持兼容性

一旦人們用您的擴展構建項目，以錯誤的方式更改它實際上會**損壞那些項目**：積木消失、參數移位、值破壞。下面的規則關於不做那樣的事。

根本原因是項目保存的方式。保存的項目通過內部標識符（擴展 ID、積木操作碼和參數名）引用您的積木，而不是它們的標籤。重命名這些標識符中的任何一個，保存的項目就無法再找到積木。

## 絕不能更改的內容

### 擴展 ID

```js
getInfo() {
  return {
    id: 'fetch', // 絕不能更改
    // ...
  };
}
```

### 積木操作碼和類型

不要重命名操作碼或改變它的用途。不要更改積木的 `blockType`，有兩個安全例外：`REPORTER` 到 `BOOLEAN`，以及 `HAT` 到 `EVENT`。其他任何更改（例如 `HAT` 到 `BOOLEAN`）都會破壞項目。要替換積木，添加一個新積木並隱藏舊的（見下文）。

### 移除積木

永遠不要刪除項目可能使用的積木。用 `hideFromPalette: true` 隱藏它。現有的副本繼續工作；它只是不再出現在積木區中。

### 參數標識符和類型

參數的鍵（`text: 'block [INPUT]'` 中的 `INPUT`）及其 `type` 不得更改或移除。

### 向現有積木添加參數

不要向已經存在的積木添加參數。而是添加一個新積木，並用新積木重新實現舊的：

```js
blocks: [
  {
    blockType: Scratch.BlockType.REPORTER,
    opcode: 'oldBlock',
    text: 'old [INPUT1]',
    arguments: { INPUT1: { /* ... */ } },
    hideFromPalette: true
  },
  {
    blockType: Scratch.BlockType.REPORTER,
    opcode: 'newBlock',
    text: 'new [INPUT1] [INPUT2]',
    arguments: { INPUT1: { /* ... */ }, INPUT2: { /* ... */ } }
  }
]
```

```js
oldBlock(args) {
  return this.newBlock({ ...args, INPUT2: 'Default value' });
}
newBlock(args) {
  // ...
}
```

### `isTerminal`

如果 `COMMAND` 積木還沒有 `isTerminal: true`，不要添加它。在下面連接了積木的現有項目會損壞。請添加一個新積木。

### 菜單上的 `acceptReporters`

永遠不要在字段（`acceptReporters: false`）和輸入（`acceptReporters: true`）之間切換菜單。它會損壞項目。創建新菜單和積木。

### 行為

瑣碎的 bug 修復通常沒問題。顯著改變積木的作用可能破壞依賴舊行為的項目。唯一可靠的保障是徹底測試。

## 可以安全更改的內容

擴展元數據：`name`、`docsURI`、`color1`/`color2`/`color3`、`menuIconURI`、`blockIconURI`。

每個積木和參數：

- `text`，只要它仍然包含相同的參數（重新排序沒問題）
- `disableMonitor`（打開它隱藏複選框但保留現有監視器）
- `hideFromPalette`
- `filter`（添加它從積木區隱藏積木但保留現有副本）
- `defaultValue`
- 圖像輸入上的 `dataURI` 和 `flipRTL`

對於菜單，您可以自由更改項目 `text`，但更改項目的 `value` 有風險。添加菜單項目總是安全的；移除它們是危險的。

## 當您確實必須破壞兼容性時

有時沒有兼容的路徑。在這種情況下，**製作一個帶新 ID 的全新擴展**，並讓舊的原樣不動。如果 `fetch` 需要重新設計，發佈 `fetch2` 並保持 `fetch` 工作。

## 下一步

接下來，C 形積木：[自定義循環和條件](/extensions/custom-c-blocks)。
