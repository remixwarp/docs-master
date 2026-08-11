---
title: 處理輸入
sidebar_position: 3
---

# 處理輸入

大多數積木將一個或多個值作為輸入（也稱為參數）。這裡有一個報告兩個值是否*嚴格*相等的積木，因此與 Scratch 的 `=` 積木不同，它將 `"a"` 和 `"A"` 視為不同（[下載](/example-extensions/strict-equality.js)）：

```js
class StrictEqualityExtension {
  getInfo() {
    return {
      id: 'strictequalityexample',
      name: 'Strict Equality',
      blocks: [
        {
          opcode: 'strictlyEquals',
          blockType: Scratch.BlockType.BOOLEAN,
          text: '[ONE] strictly equals [TWO]',
          arguments: {
            ONE: {
              type: Scratch.ArgumentType.STRING
            },
            TWO: {
              type: Scratch.ArgumentType.STRING,
              defaultValue: 'Second value'
            }
          }
        }
      ]
    };
  }

  strictlyEquals(args) {
    return args.ONE === args.TWO;
  }
}
Scratch.extensions.register(new StrictEqualityExtension());
```

## 聲明參數

向積木添加一個 `arguments` 對象。每個鍵是一個參數。鍵名可以是您喜歡的任何格式（全大寫是常見約定）。每個參數通常設置：

| 字段 | 類型 | 描述 |
|:-:|:-:|:--|
| `type` | `Scratch.ArgumentType.*` | 輸入的形狀以及默認文本框接受的內容。這只是編輯器的提示；您的代碼收到的值仍然可以是任何類型。 |
| `defaultValue` | string | 可選。在積木區中預填的值。不要設置在布爾輸入上。 |
| `menu` | string | 將輸入變成下拉框。下面介紹。 |

參數類型：

| 值 | 接受 | 示例 |
|:-:|:--|:--|
| `Scratch.ArgumentType.STRING` | 任何文本 | 蘋果, 123, true |
| `Scratch.ArgumentType.NUMBER` | 一個數字 | 123 |
| `Scratch.ArgumentType.BOOLEAN` | 一個布爾輸入槽；拒絕放入非布爾值 | true |
| `Scratch.ArgumentType.COLOR` | 十六進制顏色 | #ff4c4c |
| `Scratch.ArgumentType.ANGLE` | 方向錶盤（0 = 上，90 = 右，順時針增加） | 90 |
| `Scratch.ArgumentType.MATRIX` | 5x5 開/關網格 | 1110101010... |
| `Scratch.ArgumentType.NOTE` | 鋼琴音符選擇器 | 60 |
| `Scratch.ArgumentType.COSTUME` | 當前角色中的造型名稱 | 造型1 |
| `Scratch.ArgumentType.SOUND` | 當前角色中的聲音名稱 | 錄製1 |
| `Scratch.ArgumentType.IMAGE` | 內聯圖像，不是輸入（請參閱[雜項 API](/extensions/assorted-apis)） | 不適用 |

## 在積木中放置參數

RemixWarp 無法猜測每個輸入在標籤中的位置，因此您在 `text` 中用 `[參數名]` 標記它。每個參數必須在 `text` 中恰好出現一次。順序無關緊要。

積木運行時，您的函數將接收一個對象作為第一個參數，其中每個參數都有一個屬性。習慣上叫它 `args`，或解構它：

```js
// 使用 args.X
goto(args) {
  console.log(args.X, args.Y);
}

// 或解構
goto({X, Y}) {
  console.log(X, Y);
}
```

參數的值可以是字符串、數字或布爾值，**與聲明的 `type` 無關**。類型是對編輯器的建議，絕不是保證。您的代碼必須自己轉換值，例如用 [`Scratch.Cast`](/extensions/assorted-apis#scratchcast)。

## 靜態菜單

要給輸入一個固定選擇的下拉框，將其 `type` 設置為 `Scratch.ArgumentType.STRING`，添加一個命名菜單的 `menu`，並在 `menus` 對象中定義該菜單（[下載](/example-extensions/strings-1.js)）：

```js
class Strings1 {
  getInfo() {
    return {
      id: 'strings1example',
      name: 'Encoding',
      blocks: [
        {
          opcode: 'convert',
          blockType: Scratch.BlockType.REPORTER,
          text: 'convert [TEXT] to [FORMAT]',
          arguments: {
            TEXT: {
              type: Scratch.ArgumentType.STRING,
              defaultValue: 'Apple'
            },
            FORMAT: {
              type: Scratch.ArgumentType.STRING,
              menu: 'FORMAT_MENU'
            }
          }
        }
      ],
      menus: {
        FORMAT_MENU: {
          acceptReporters: true,
          items: ['uppercase', 'lowercase']
        }
      }
    };
  }

  convert(args) {
    // TEXT 可能是數字或布爾值，所以在對它調用字符串方法
    // 之前先轉換為字符串。
    if (args.FORMAT === 'uppercase') {
      return args.TEXT.toString().toUpperCase();
    } else {
      return args.TEXT.toString().toLowerCase();
    }
  }
}
Scratch.extensions.register(new Strings1());
```

每個菜單是一個帶有以下內容的對象：

| 字段 | 類型 | 描述 |
|:-:|:-:|:--|
| `items` | array | 字符串，或 `{text, value}` 對象（見下文）。不能為空。 |
| `acceptReporters` | boolean | 積木是否可以放入菜單。幾乎總是將其設置為 `true`。 |

這裡有一個重要區別。`acceptReporters: true` 的菜單是一個**輸入**：用戶可以向其中放入任何報告積木。`acceptReporters: false` 的菜單是一個**字段**：它只能始終是固定字符串之一。您幾乎總是想要一個輸入。唯一常見的例外是[事件帽子積木](/extensions/hats)，它們只支持字段菜單。

::::warning
在字段和輸入之間切換菜單（更改 `acceptReporters`）是向後不兼容的更改，會損壞現有項目。提前決定。請參閱[保持兼容性](/extensions/compatibility)。
::::

將菜單直接設置為數組（而不是對象）會隱式地使它成為字段。避免這樣做；總是使用帶 `acceptReporters: true` 的對象形式。

## 分離顯示文本和值

有時下拉框中顯示的標籤應該與您的代碼收到的值不同。對這些項目使用 `{text, value}` 對象（[下載](/example-extensions/strings-2.js)）：

```js
menus: {
  FORMAT_MENU: {
    acceptReporters: true,
    items: [
      { text: 'UPPERCASE', value: 'up' },
      { text: 'lowercase', value: 'low' }
    ]
  }
}
```

下拉框顯示"UPPERCASE"，但積木收到 `"up"`。

## 練習

1. 添加一個像 Scratch 的 `連接` 積木一樣將兩個參數連接成一個字符串的積木。將兩者都轉換為字符串，使 `連接 ((1 + 2)) ((3 + 4))` 得到 `"37"`，而不是 10。
2. 添加一個帶數字輸入和"奇"、"偶"菜單的布爾積木，按菜單所說的報告數字是奇數還是偶數。

## 下一步

到目前為止積木幾乎立即完成。接下來，[如果一個積木需要等待某些東西](/extensions/async)，比如網絡請求呢？
