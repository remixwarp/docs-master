---
title: 高級編譯技巧
sidebar_position: 5
---

# 高級編譯技巧

本頁涵蓋[`compiler.register` API](/extensions/compiled/structure) 超出普通報告積木的部分：命令積木、字段、可變參數輸入、原始輸入和接觸運行時狀態。這裡的一切都對照 RemixWarp 自己的內置運算積木的編譯方式驗證過。

請牢記思維模型：`compile` **在編譯時運行一次**，並返回**一個 JavaScript 字符串**。它自己不能做運行時工作；它決定生成的代碼將做什麼運行時工作。任何必須響應運行中項目的東西都必須位於您返回的字符串內部。

## 命令積木

給描述符 `type: COMMAND`。您返回的字符串用作語句（編譯器附加 `;`），因此返回帶副作用的表達式：

```js
compiler.register('myext', {
  logmessage: {
    type: T.COMMAND,
    compile: ({ input }) => `console.log(${input.string('MESSAGE')})`
  }
});
```

要運行多個語句，將它們包裹在立即調用函數中：

```js
compile: ({ input, target }) =>
  `(() => { const n = ${input.number('N')}; ${target}.setXY(n, n); })()`
```

## 接觸運行時、目標和舞臺

上下文給您指代生成作用域中引擎對象的變量名。將它們插值到您的源中：

```js
compiler.register('myext', {
  stagewidth: {
    type: T.NUMBER,
    compile: ({ runtime }) => `${runtime}.stageWidth`
  },
  myx: {
    type: T.NUMBER,
    compile: ({ target }) => `${target}.x`
  }
});
```

`runtime` 是運行時，`target` 是運行積木的目標，`stage` 是舞臺。例如，內置舞臺寬度積木編譯為返回 `runtime.stageWidth` 的模板。

## 字段

`field(name)` 返回已 JSON 編碼的字段值，因此作為字符串字面量拼接是安全的：

```js
compile: ({ field }) => `someTable[${field('CHOICE')}]`
// 如果 CHOICE 字段是 "red"，這變成：someTable["red"]
```

## 輸入轉換

選擇與您的 JavaScript 期望匹配的轉換。選擇正確的避免輸出中的冗餘轉換。

| 輔助工具 | 發出 |
|:--|:--|
| `input('A')` | 輸入，轉換為"any"。 |
| `input.number('A')` | 轉換為數字。 |
| `input.numberOrNaN('A')` | 轉換為可能為 `NaN` 的數字。 |
| `input.string('A')` | 轉換為字符串。 |
| `input.boolean('A')` | 轉換為布爾值。 |
| `input.raw('A')` | 無轉換。對於運算符下拉框，這是裸運算符文本。 |

`input.raw` 是將運算符作為字段的積木構建表達式的方式。內置比較積木正是這樣做的：

```js
compare: {
  type: T.BOOLEAN,
  compile: ({ input: i }) => `(${i.number('A')} ${i.raw('C')} ${i.number('B')})`
}
// 使用 C = "<"，這變成：(a < b)
```

只對您控制的值或固定菜單使用 `raw`。將任意的用戶字符串作為原始源拼接是注入風險。

## 可變參數輸入

接受可變數量輸入的積木（如幾個值的 `最小`/`最大`）從 `mutation` 讀取數量。這是 RemixWarp 編譯其可變參數 `min` 和 `max` 的逐字方式：

```js
const variadic = (name, input, mutation) => {
  const count = Math.max(2, parseInt(mutation.itemcount, 10) || 2);
  const parts = Array.from({ length: count }, (_, i) => input.number(`NUM${i + 1}`));
  return `Math.${name}(${parts.join(',')})`;
};

compiler.register('myext', {
  min: { type: T.NUMBER, compile: ({ input, mutation }) => variadic('min', input, mutation) },
  max: { type: T.NUMBER, compile: ({ input, mutation }) => variadic('max', input, mutation) }
});
```

## 選擇結果類型

`type` 是積木產生的值，編譯器用它來跳過消耗您輸出的積木中的轉換。要誠實：

- 只在結果總是真正的數字時使用 `NUMBER`。如果它可能是 `NaN`（可能失敗的解析），使用 `NUMBER_OR_NAN`，否則編譯器可能假設有效數字並跳過調用者需要的 `NaN` 保護。
- 當您無法承諾類型時使用 `ANY`，例如 `JSON.parse` 結果。

```js
jsonparse: { type: T.ANY, compile: ({ input: i }) => `JSON.parse(${i.string('A')})` }
```

## 優先級和括號

輸入展開為整個表達式，而不僅僅是字面量，因此在運算符優先級可能改變含義的任何地方加上括號。優先包裹輸入和整個結果：

```js
// 有風險：輸入可能是 `a + b`
compile: ({ input: i }) => `${i.number('X')} ** 2`
// 安全
compile: ({ input: i }) => `((${i.number('X')}) ** 2)`
```

## 保持回退同步

每個編譯積木仍然需要它的解釋器方法（請參閱[您的第一個編譯擴展](/extensions/compiled/first-extension)）。它在積木未編譯時運行，因此必須計算相同的結果。當您更改編譯邏輯時，也要更改回退。

## 不要做什麼

編譯器故意很窄，這就是重點。它沒有受支持的 API 用於多遍編譯、將共享輔助函數提升到輸出中、掛鉤編譯器的生命週期，或在編譯時保持跨積木狀態。如果您發現自己想要這些，積木可能太大而不值得編譯；請改為將其寫為普通的[非沙箱積木](/extensions/unsandboxed)。

## 另請參閱

- [編譯擴展概覽](/extensions/compiled/overview)
- [遺留補丁方法](/extensions/compiled/patching)
