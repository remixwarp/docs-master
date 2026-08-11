---
title: 自定義 C 積木
sidebar_position: 9
---

# 自定義 C 積木

C 積木是包裹其他積木的那些：`如果`、`如果/否則`、`重複執行`、`重複執行無限次`。RemixWarp 讓擴展定義自己的 C 積木。

::::warning
自定義 C 積木只在[非沙箱擴展](/extensions/unsandboxed)中工作。
::::

## 兩種積木類型

- 用於重複積木的 `Scratch.BlockType.LOOP`。它恰好有一個分支，因此 `branchCount` 是隱含的。
- 用於 `如果`/`否則` 風格積木的 `Scratch.BlockType.CONDITIONAL`。將 `branchCount` 設置為它控制的分支數。

對沒有底部連接的積木（如 `重複執行無限次`）使用 `isTerminal: true`。

## 驅動分支

有兩種方式控制運行哪個分支以及是否循環。

**從積木函數返回一個值：**

- `CONDITIONAL`：返回要運行的分支的從 1 開始的索引，或 `0` / 假值表示不運行任何分支。
- `LOOP`：返回 `true` 運行分支並再次循環，或假值停止。

**或顯式調用 `util.startBranch(branchIndex, isLoop)`：**

- `branchIndex`（數字）：要運行的從 1 開始的分支。第一個分支是 `1`。
- `isLoop`（布爾值）：如果為 `true`，分支完成後再次調用積木函數。

## 示例：如果 / 否則

```js
class ConditionalExtension {
  getInfo() {
    return {
      id: 'conditionalexample',
      name: 'Conditionals',
      blocks: [
        {
          opcode: 'myIfElse',
          text: ['if [CONDITION] then', 'else'],
          blockType: Scratch.BlockType.CONDITIONAL,
          branchCount: 2,
          arguments: {
            CONDITION: { type: Scratch.ArgumentType.BOOLEAN }
          }
        }
      ]
    };
  }

  myIfElse(args, util) {
    if (args.CONDITION) {
      util.startBranch(1); // "如果" 分支
    } else {
      util.startBranch(2); // "否則" 分支
    }
  }
}
Scratch.extensions.register(new ConditionalExtension());
```

用返回風格編寫的相同積木：

```js
myIfElse(args) {
  return args.CONDITION ? 1 : 2; // 從 1 開始的分支索引
}
```

注意 `text` 是一個數組。對於多分支積木，每個字符串是一個分支上方的標籤。

## 示例：循環

```js
class LoopExtension {
  getInfo() {
    return {
      id: 'loopexample',
      name: 'Loops',
      blocks: [
        {
          opcode: 'foreverLoop',
          text: 'run forever',
          blockType: Scratch.BlockType.LOOP,
          isTerminal: true // 下面沒有連接
        },
        {
          opcode: 'repeatUntil',
          text: 'repeat until [CONDITION]',
          blockType: Scratch.BlockType.LOOP,
          arguments: {
            CONDITION: { type: Scratch.ArgumentType.BOOLEAN }
          }
        }
      ]
    };
  }

  foreverLoop(args, util) {
    util.startBranch(1, true); // 運行分支 1，然後循環
  }

  repeatUntil(args, util) {
    if (!args.CONDITION) {
      util.startBranch(1, true); // 條件為假：運行並再次循環
    }
    // 條件為真：什麼都不做，循環結束
  }
}
Scratch.extensions.register(new LoopExtension());
```

計數 `重複執行` 使用返回風格和 `util.stackFrame` 來保持每次循環的狀態：

```js
repeatTimes(args, util) {
  const times = Math.round(Scratch.Cast.toNumber(args.TIMES));
  if (typeof util.stackFrame.loopCounter === 'undefined') {
    util.stackFrame.loopCounter = times;
  }
  util.stackFrame.loopCounter--;
  return util.stackFrame.loopCounter >= 0; // true = 再次運行分支
}
```

`util.stackFrame` 是綁定到這個特定積木調用的暫存空間。它是存儲循環計數器的正確位置，因為它在積木完成時被清除，並且不會與其他積木副本衝突。

## 要記住的事情

1. **分支從 1 開始。** 第一個分支是 `1`，不是 `0`。
2. **循環參數重新求值。** 在 `LOOP` 中，每次積木運行時都會再次讀取輸入，因此 `重複執行直到 [x = 5]` 會看到 `x` 的當前值。
3. **`startBranch` 讓出。** 執行傳遞給分支；分支完成後（如果循環）再次調用您的函數。
4. **`isTerminal` 不是"停止"。** 它只是防止在下面連接積木。如果終止積木位於循環末尾，循環仍然繼續，除非有東西停止線程。

## 下一步

接下來，一些[高級積木自定義](/extensions/advanced-block-customization)技巧。
