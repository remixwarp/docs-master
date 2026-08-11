---
title: renderer.destroySkin()
---

# renderer.destroySkin()

銷燬一個皮膚並釋放其資源。調用此方法後，請勿再使用該皮膚或其 ID。

## 語法

```javascript
renderer.destroySkin(skinId)
```

## 參數

### skinId
**類型：** `number`

要銷燬的皮膚 ID。

## 返回值

**類型：** `void`

## 示例

```javascript
class SkinManagerExtension {
  constructor(runtime) {
    this.runtime = runtime;
    this.customSkins = new Map();
    
    // Clean up on project stop
    runtime.on('PROJECT_STOP_ALL', () => {
      this.cleanup();
    });
  }
  
  cleanup() {
    const renderer = this.runtime.renderer;
    
    // Destroy all custom skins
    for (const skinId of this.customSkins.values()) {
      renderer.destroySkin(skinId);
    }
    
    this.customSkins.clear();
  }
}
```

## 重要說明

- **內存管理** - 不再需要時一定要銷燬皮膚
- **可繪製對象引用** - 銷燬被可繪製對象使用的皮膚可能導致渲染問題
- **最佳實踐** - 在銷燬皮膚之前，先恢復（還原）使用該皮膚的可繪製對象

## 另請參閱

- [createBitmapSkin()](./createBitmapSkin.md) - 創建位圖皮膚
- [createSVGSkin()](./createSVGSkin.md) - 創建 SVG 皮膚
- [資源管理](../../concepts/resource-management.md) - 清理的最佳實踐
