---
title: 雜項 API
sidebar_position: 12
---

# 雜項 API

既然您可以編寫擴展，這裡有 `getInfo()` 和 `Scratch` 對象上可用的更多選項。除非另有說明，這些在**沙箱和非沙箱**擴展中都有效，並且可以自由組合。

## 積木顏色

`color1`、`color2` 和 `color3` 分別設置積木顏色、輸入顏色和菜單顏色。`color1` 應該最亮，`color3` 最暗。使用十六進制代碼（[下載](/example-extensions/color.js)）：

```js
getInfo() {
  return {
    id: 'colorexample',
    name: 'Color Example',
    color1: '#ff0000',
    color2: '#00ff00',
    color3: '#0000ff',
    blocks: [ /* ... */ ]
  };
}
```

替代積木顏色模式（高對比度、深色和插件預設）會自動從這些值生成。

## docsURI

`docsURI` 在擴展積木列表的頂部添加一個打開文檔頁面的按鈕：

```js
getInfo() {
  return {
    id: 'hellodocs',
    name: 'Hello Docs!',
    docsURI: 'https://example.com/my-extension-docs',
    blocks: [ /* ... */ ]
  };
}
```

## disableMonitor

RemixWarp 自動為任何無輸入的 `REPORTER` 積木（並且與 Scratch 不同，`BOOLEAN` 積木也是）提供一個監視器複選框。在積木上設置 `disableMonitor: true` 來隱藏該複選框（[下載](/example-extensions/unmonitorable.js)）。注意這不會移除有人用擴展舊版本創建的監視器。

## Scratch.Cast

Scratch 有自己的類型轉換和比較規則，帶有許多怪癖。與其重新發明它們，不如使用 `Scratch.Cast`（[下載](/example-extensions/cast.js)）：

```js
toNumber({INPUT})   { return Scratch.Cast.toNumber(INPUT); }
castToString({INPUT}) { return Scratch.Cast.toString(INPUT); }
toBoolean({INPUT})  { return Scratch.Cast.toBoolean(INPUT); }

compare({A, B}) {
  const c = Scratch.Cast.compare(A, B);
  // 使用 < 0、> 0 或 === 0。不要使用 === 1 或 === -1。
  if (c === 0) return 'Equal';
  return c > 0 ? 'A is greater' : 'B is greater';
}
```

完整的參考在[實用 API 頁面](/extensions/apis/utility-apis)。

## hideFromPalette

`hideFromPalette: true` 從積木區隱藏積木而不移除它，因此項目中已有的副本繼續工作。這是[向後兼容更改](/extensions/compatibility)的主要工具。加載 [hidden-1.js](/example-extensions/hidden-1.js) 並保存一個使用其積木的項目，然後加載 [hidden-2.js](/example-extensions/hidden-2.js)（同一擴展，積木現在隱藏）並重新打開項目：現有積木仍然運行，但它從積木區消失了。

## filter

如果積木只在角色中有意義，或只在舞臺中有意義，將 `filter` 設置為包含 `Scratch.TargetType.SPRITE` 或 `Scratch.TargetType.STAGE` 的數組（[下載](/example-extensions/filter.js)）：

```js
{
  opcode: 'sprites',
  blockType: Scratch.BlockType.COMMAND,
  text: 'available in ONLY sprites',
  filter: [Scratch.TargetType.SPRITE]
}
```

`filter` 隻影響積木顯示在哪個積木區。通過拖放或背包仍可能最終把積木放到"錯誤"的目標中，因此在重要時您的代碼仍必須檢查 `util.target.isStage`。要完全隱藏積木，使用 `hideFromPalette`，而不是 `filter: []`。

## 圖標

有三種附加圖像的方式：

- 擴展上的 `menuIconURI`：積木區中顯示的圖像。回退到 `blockIconURI`，然後是彩色圓圈。
- 擴展上的 `blockIconURI`：每個積木上的默認圖標。
- 積木上的 `blockIconURI`：覆蓋該積木的擴展圖標。

每個都必須是 [data: URL](https://developer.mozilla.org/zh-CN/docs/Web/HTTP/Basics_of_HTTP/Data_URLs)。首選 SVG；至少 64x64 的 PNG 或 JPG 也可以。保持正方形。請參閱 [icons.js](/example-extensions/icons.js)。

## 內聯圖像

通過添加類型為 `Scratch.ArgumentType.IMAGE` 且帶 `dataURI` 的參數，將圖像放入積木內部。設置 `flipRTL: true` 在從右到左的語言中鏡像它。請參閱 [inline-images.js](/example-extensions/inline-images.js)。

## 分隔符

要在積木區中分隔積木組，請將字符串 `'---'` 放入 `blocks` 數組（[下載](/example-extensions/separators.js)）：

```js
blocks: [
  { opcode: 'block1', blockType: Scratch.BlockType.COMMAND, text: 'group 1' },
  '---',
  { opcode: 'block2', blockType: Scratch.BlockType.COMMAND, text: 'group 2' }
]
```

## 終止積木

`isTerminal: true` 阻止另一個積木連接到 `COMMAND` 積木的下面（[下載](/example-extensions/terminal.js)）。它看起來像"停止全部"，但它不會停止腳本；它只阻擋底部連接。循環末尾的終止積木不會自行停止循環。

## 下一步

接下來，[事件和帽子積木](/extensions/hats)（如果您跳過了），或[API 參考頁面](/extensions/apis/scratch-api)瞭解 `Scratch` 對象、VM、渲染器和音頻引擎的完整表面。
