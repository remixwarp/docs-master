---
title: 快速入门
sidebar_position: 2
---

# 快速入门

RemixWarp 是一个基于 Web 的应用，可直接在浏览器中运行。无需安装！

## 访问 RemixWarp

RemixWarp 仅作为 Web 应用提供，可通过以下地址访问：

**🌐 [https://github.com/RemixWarp/scratch-gui/issues)**

只需在任何现代浏览器中打开该链接，即可开始创建！

## 系统要求

RemixWarp 可在任何支持 JavaScript 和 WebGL 的现代浏览器中运行：

### 支持的浏览器
- **Chrome 80+**（推荐，性能最佳）
- **Firefox 78+**
- **Safari 14+**（macOS/iOS）
- **Edge 80+**

### 硬件要求
- **内存**：最低 2GB，复杂项目建议 4GB+
- **网络**：加载和保存项目需要稳定连接
- **存储**：项目保存在浏览器的本地存储或云端存储中

### 推荐配置
- **内存**：对于包含大量角色和脚本的大型项目建议 4GB+
- **处理器**：现代多核处理器以获得流畅性能
- **网络**：宽带连接以加快项目加载速度
- **显卡**：支持 WebGL 2.0 以获得最佳渲染效果

## 浏览器兼容性

| 浏览器 | 最低版本 | 推荐版本 |
|---------|----------------|-------------|
| Chrome | 80+ | 最新版 |
| Firefox | 78+ | 最新版 |
| Safari | 14+ | 最新版 |
| Edge | 80+ | 最新版 |

### 必需功能
- ES2020 支持
- WebGL 1.0（推荐 WebGL 2.0）
- Web Audio API
- 本地存储
- WebAssembly（以获得最佳性能）

## 首次设置

首次访问 RemixWarp 时：

1. **打开浏览器**并导航至 [remixwarp.pages.dev](https://github.com/RemixWarp/scratch-gui/issues)
2. **允许 JavaScript**（如果提示，RemixWarp 运行必需）
3. **接受摄像头/麦克风权限**（如果计划使用侦测积木）
4. **创建账户**（可选）以将项目保存到云端

## 浏览器配置

### 启用所需功能

为获得最佳 RemixWarp 体验，请确保以下浏览器功能已启用：

- **JavaScript**：所有功能必需
- **WebGL**：舞台渲染和特效需要
- **本地存储**：用于在本地保存项目
- **摄像头/麦克风**：侦测积木需要（可选）

### 性能提示

- **关闭不必要的标签页**以释放内存
- **启用硬件加速**（如果浏览器设置中可用）
- **定期清除浏览器缓存**（如果 RemixWarp 变慢）
- **禁用可能干扰性能的浏览器扩展**

## 开发设置

对于想要修改或为 RemixWarp 做贡献的开发者：

### 前提条件
- Node.js 18+ 
- npm 或 yarn
- Git

### 克隆和构建

```bash
# 克隆仓库
git clone https://github.com/RemixWarp/scratch-gui/issues
cd scratch-gui

# 安装依赖
npm ci

# 启动开发服务器
npm start
```

开发服务器将在 `https://github.com/RemixWarp/scratch-gui/issues

### 构建其他组件

要处理完整的 RemixWarp 技术栈：

```bash
# 克隆所有仓库
git clone https://github.com/RemixWarp/scratch-gui/issues
git clone https://github.com/RemixWarp/scratch-gui/issues  
git clone https://github.com/RemixWarp/scratch-gui/issues

# 链接本地包（在每个目录中）
cd scratch-vm && npm link
cd ../scratch-render && npm link
cd ../scratch-gui && npm link scratch-vm scratch-render

# 开始开发
cd scratch-gui && npm start
```

## 故障排查

### 常见问题

**RemixWarp 无法加载：**
1. 检查网络连接
2. 临时禁用浏览器扩展
3. 清除浏览器缓存和 Cookie
4. 尝试其他浏览器

**性能不佳：**
1. 关闭其他浏览器标签页
2. 重启浏览器
3. 检查可用内存
4. 尝试使用 Chrome 以获得最佳性能
5. 在浏览器设置中启用硬件加速

**项目无法保存：**
1. 检查浏览器本地存储是否已满
2. 如果使用云保存，请启用第三方 Cookie
3. 创建账户以进行云端存储

**积木缺失或行为异常：**
1. 刷新页面
2. 清除浏览器缓存
3. 检查浏览器控制台错误

**图形/渲染问题：**
1. 更新显卡驱动程序
2. 在浏览器设置中启用 WebGL
3. 尝试其他浏览器

### 获取帮助

如果遇到问题：
- 查看[故障排查指南](../user-guide/troubleshooting.md)
- 访问我们的[社区论坛](https://github.com/RemixWarp/scratch-gui/issues)
- 在 [GitHub Issues](https://github.com/RemixWarp/scratch-gui/issues) 上报告缺陷

## 接下来做什么？

现在你可以访问 RemixWarp 了：

1. **[快速入门指南](./quick-start.md)** - 创建你的第一个项目
2. **[用户界面](../user-guide/interface.md)** - 了解界面
3. **[项目管理](../user-guide/projects.md)** - 保存和分享项目
4. **[迁移指南](./migrating-from-scratch.md)** - 导入现有的 Scratch 项目

*继续阅读[快速入门](./quick-start.md)以创建你的第一个项目。*
