---
hide_table_of_contents: true
---

# 提交擴展

如果您想將擴展提交到 [extensions.bilup.org](https://github.com/RemixWarp/extensions/)，您需要遵循以下規則：

::::info
除非它是一個**高質量**的擴展，否則我們不會為您修改文件。
::::

## 擴展封面圖

每個擴展都需要一張封面圖，存儲在 `images/` 目錄中。
此外，封面圖名稱必須與擴展文件名相同，尺寸為 600x300，格式為 `.svg`。

## 擴展文件

### 頭部

擴展的頭部部分必須包含以下內容：

```javascript
// Name: ExtensionName
// ID: extensionid
// Description: ExtensionDescription
// By: Name <your url>
// Original: TheOriginalAuthor <original url>
// License: MPL-2.0
```

您必須使用行註釋；塊註釋 `/* */` 不會生效。這些字段是**必需的**：

- `Name` 出現在網站和畫廊中。它應該與 getInfo() 返回的 `name` 相似。
- `ID` 必須與 getInfo() 返回的 `id` 完全相同，並且必須是**小寫**。
- `Description` 出現在網站和畫廊中。
- `License` 描述擴展代碼使用的許可證。它必須是有效的 [SPDX 許可證](https://spdx.org/licenses/) 表達式。對於我們推薦的 Mozilla Public License 2.0，標識符是 `MPL-2.0`。
- `By` 用於署名作者。`Original` 用於基於他人作品的擴展。它們都使用相同的格式：`Name` 或 `Name <Url>`（URL 必須是**有效的**）。如果您想署名多個作者，只需再添加一條 `// By: ...` 或 `// Original: ...` 註釋。

### 代碼

提交前，請確保您的擴展代碼**沒有錯誤**。

我們建議檢查以下內容：
- 檢查您的擴展是否存在於 `extensions\extensions.json` 中
- 檢查您的封面圖是否存在於 `images/` 目錄中
- 運行 `npm start` 或 `npm run build` 檢查構建錯誤

### 國際化翻譯

我們要求您的擴展包含**國際化翻譯**（`zh-CN` 和 `en`；未來可能添加更多語言）。

國際化翻譯文件存儲在 `translations/` 目錄中，其中 `translations\extension-metadata.json` 存儲名稱和描述的翻譯，`translations\extension-runtime.json` 存儲擴展代碼的翻譯。

每個翻譯必須遵循此格式：
```json
"zh-CN": {
  "extensionID@translationsID": "value"
}
```
其中 `extensionID` 是您擴展的 ID，`translationsID` 是翻譯鍵，`value` 是翻譯後的文本。

在代碼中使用國際化翻譯時，您需要使用 `Scratch.translate()` 方法。
```javascript
Scratch.translate({ default: 'defaultValue', id: 'translationsID' });
```
通常，`defaultValue` 應包含英文翻譯。

注意：`translationsID` 是您之前在 `translations\extension-runtime.json` 中定義的鍵。調用時**不要**使用 `extensionID@translationsID`。

我們建議以標準化的方式定義 `translationsID`，例如 `group.tools`、`block.settings` 等。

## 關於 **AI** 的聲明

- 我們允許您使用 AI 編寫代碼，但我們建議您不要**過度依賴** AI。
如果您使用 AI 編寫代碼，請確保您能**理解** AI 生成的代碼，並且能在沒有 AI 的情況下修復問題。
- 我們**不建議**使用 AI 生成封面圖。

## 提交您的擴展

我們建議以下提交方法：

- 直接將您的擴展提交到 `extensions` 倉庫（這可能要求您擁有提交到 `extensions` 倉庫的**權限**；我們不推薦此方法）
- 創建分支並提交到該分支（不推薦）
- 準備您的擴展並將其發送給我們的維護者（推薦）

有關提交擴展的更多詳情，請**聯繫我們**（support@RemixWarp.org）。
