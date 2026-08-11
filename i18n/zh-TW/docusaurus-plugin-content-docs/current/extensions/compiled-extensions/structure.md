---
title: 擴展結構
sidebar_position: 2
---

# 擴展結構

編譯擴展是一個普通擴展加上一次 `Scratch.vm.exports.compiler.register` 調用。本頁介紹該調用的形狀。[下一頁](/extensions/compiled/first-extension)構建一個完整示例。

## 骨架

```js
(function(Scratch) {
  'use strict';
  if (!Scratch.extensions.unsandboxed) {
    throw new Error('This extension must run unsandboxed');
  }

  const { vm, BlockType, ArgumentType } = Scratch;
  const { compiler } = vm.exports;
  const T = compiler.types; // ANY, NUMBER, NUMBER_OR_NAN, STRING, BOOLEAN, COMMAND

  // 1. 告訴編譯器如何為每個積木生成 JavaScript。
  compiler.register('mathutils', {
    square: {
      type: T.NUMBER,
      compile: ({ input }) => `(${input.number('NUMBER')} ** 2)`
    }
  });

  // 2. 正常註冊擴展，每個積木帶一個回退 func。
  class MathUtils {
    getInfo() {
      return {
        id: 'mathutils',
        name: 'Math Utils',
        blocks: [
          {
            opcode: 'square',
            blockType: BlockType.REPORTER,
            text: 'square of [NUMBER]',
            arguments: { NUMBER: { type: ArgumentType.NUMBER, defaultValue: 5 } }
          }
        ]
      };
    }
    // 解釋器回退：積木未編譯時運行。
    square(args) {
      return Scratch.Cast.toNumber(args.NUMBER) ** 2;
    }
  }
  Scratch.extensions.register(new MathUtils());
})(Scratch);
```

這裡發生兩次獨立的註冊。`compiler.register` 教編譯器；`Scratch.extensions.register` 將積木添加到積木區並提供解釋器回退。積木的 `opcode`（`square`）和擴展 `id`（`mathutils`）將它們聯繫在一起：在內部，編譯器條目以 `mathutils_square` 為鍵，這正是積木的完整操作碼。

## compiler.register(extensionId, blocks)

- `extensionId`：您擴展的 `id`，與您在 `getInfo` 中傳遞的相同字符串。
- `blocks`：將每個積木的 `opcode` 映射到描述符的對象。

每個描述符具有：

| 字段 | 描述 |
|:--|:--|
| `type` | `compiler.types` 之一。是積木產生的值的類型（堆疊積木為 `COMMAND`）。 |
| `compile` | 一個為積木返回**JavaScript 源字符串**的函數。 |

`compiler.types`：

| 類型 | 用於 |
|:--|:--|
| `NUMBER` | 總是產生數字的報告積木。 |
| `NUMBER_OR_NAN` | 產生可能為 `NaN` 的數字的報告積木。 |
| `STRING` | 產生字符串的報告積木。 |
| `BOOLEAN` | 布爾報告積木。 |
| `ANY` | 類型事先不知道的報告積木。 |
| `COMMAND` | 運行操作且不返回任何內容的堆疊積木。 |

選擇特定類型幫助編譯器在下游跳過冗餘轉換，因此請選擇您的積木真正保證的最窄類型。

## 編譯上下文

`compile` 接收一個對象：

```js
compile: ({ input, field, mutation, runtime, target, stage }) => `...`
```

| 屬性 | 它給您什麼 |
|:--|:--|
| `input(name)` | 輸入 `name` 的 JavaScript 源，轉換為"any"。 |
| `input.number(name)` | 轉換為數字的輸入源。 |
| `input.string(name)` | 轉換為字符串的輸入源。 |
| `input.boolean(name)` | 轉換為布爾值的輸入源。 |
| `input.numberOrNaN(name)` | 轉換為可能為 `NaN` 的數字的輸入源。 |
| `input.raw(name)` | 無轉換的輸入源。對於字面量，這是裸值。 |
| `field(name)` | 字段 `name` 的值，已 JSON 編碼（作為字符串字面量放入源是安全的）。 |
| `mutation` | 積木的 mutation 對象（用於可變參數積木）。 |
| `runtime`、`target`、`stage` | 指代生成代碼中運行時、當前目標和舞臺的變量名（作為字符串）。用它們接觸引擎狀態。 |

關鍵的思維模型：`compile` 在編譯時運行並返回**文本**。`input.*` 輔助工具返回文本（一個 JavaScript 表達式），您通過字符串插值組裝更大的表達式。您返回的內容被拼接到編譯腳本中並在運行時執行。

## 真實的內置示例

RemixWarp 自己的運算積木正是以這種方式註冊的。幾個，直接來自引擎：

```js
// 數字結果
power:   ({ input: i }) => `Math.pow(${i.number('A')}, ${i.number('B')})`,
clamp:   ({ input: i }) => `Math.min(Math.max(${i.number('A')}, ${i.number('B')}), ${i.number('C')})`,

// 布爾結果
notequals: ({ input: i }) => `(${i.string('A')} !== ${i.string('B')})`,
starts:    ({ input: i }) => `(${i.string('A')}).startsWith(${i.string('B')})`,

// 字符串結果
replaceall: ({ input: i }) => `(${i.string('A')}).replaceAll(${i.string('C')}, ${i.string('B')})`,

// 接觸運行時狀態
stagewidth: ({ runtime }) => `${runtime}.stageWidth`,

// 無輸入
pi: () => 'Math.PI',
```

`compile` 必須返回一個字符串。在優先級可能咬到您時用括號包裹表達式：輸入可能展開為類似 `a + b` 的東西，而 `$(i.number('A')) ** 2` 在輸入周圍沒有括號會解析錯誤。

## 回退函數

積木仍然需要類中的普通方法（上面的 `square(args)`）。它在積木未編譯時運行：當報告積木供給監視器時、編譯器被禁用時，或任何沒有 RemixWarp 編譯器的環境中。保持回退行為與編譯版本相同，使結果永遠不會不同。

## 下一步

端到端[構建第一個編譯擴展](/extensions/compiled/first-extension)。
