---
title: 其他独有插件
sidebar_position: 10
---

# 其他独有插件

RemixWarp 还提供了一系列 RemixWarp 中不存在的独立插件（Addons）。

## 1. 批量颜色替换（Batch Color Replace）

批量替换当前角色所有造型中的指定颜色。

**功能：**
- 在颜色选择器面板添加"批量替换"按钮（绿色）
- 点击后弹出 prompt 输入新颜色（`#RRGGBB` 格式）
- 支持 SVG 造型（位图/PNG 暂未实现）

## 2. 代码风格（Coder Style）

极简主义积木风格——仅彩色文本、无可见边框、输入框采用括号风格。

**设置项：**
- `block-opacity`：积木透明度（默认 0.02）
- `c-shape-opacity`：C 形积木透明度
- `boolean-opacity`：布尔积木透明度
- `input-opacity`：输入积木透明度

## 3. VS Code 注释同步（Comment VSCode Sync）

在 Scratch 编辑器与 VS Code 之间同步注释（通过 WebSocket 连接 VS Code 扩展调试服务）。

**功能：**
- 检测 `window.ScratchExtensionDebug` 连接状态
- 同步工作区注释与积木注释

## 4. 语言包管理（Language Package）

允许加载和管理额外的语言包。

**功能：**
- 在"编辑"菜单添加"语言包管理"菜单项（lucide-globe 图标）
- 打开 850×600 的窗口（WindowManager）
- 配合 `services/LanguageService.js` 实现：
  - 加载/保存用户上传的语言包（localStorage `userLanguagePackages`）
  - 生成包含全部翻译键的语言包模板
  - 上传语言包校验（locale/name/translations 必填）
  - 多级回退翻译（用户包 → 系统文件 → 默认英文 → 原始键名）
  - 生成可用语言列表（支持用户自定义 locale，如 `zh-cn-custom`）

**设置项：** `languagePackage`（启用语言包，默认开启）

## 5. 视频录制（Media Recorder）

在编辑器菜单栏添加"开始录制"按钮，录制项目舞台画面为视频。

**功能：**
- 菜单栏录制按钮
- 环境不支持 MediaRecorder 时标记为 `unsupported`

## 6. 自制积木增强（My Blocks Plus）

增强自定义积木（"我的积木"）的功能和灵活性。

**功能：**
- 创建项目时自动加载"我的积木增强"扩展
- 可隐藏自定义积木分类（`hideCustomBlocks` 设置）
- 隐藏 `scratchCategoryId-more` 分类

**警告：** 会加载新扩展，且无法从扩展管理器移除。

## 7. 舞台相机（Stage Camera）

为舞台添加相机控制功能，支持缩放、平移和全屏。使用视频侦测或人脸检测扩展时特别有用。

**功能：**
- 舞台选择器区域添加相机控制面板：放大/缩小/重置按钮、窗口模式按钮、缩放百分比输入框

**设置项：**
- `showControls`：显示相机控制（默认 false）
- `autoHide`：不使用时自动隐藏

## 8. 视频弹窗（Video Modal）

视频教程播放弹窗，读取 `modals.videoModal` 与 `modals.videoModalData`（教程数据）。

## 9. 教程弹窗（Tutorial Modal）

教程内容弹窗，读取 `modals.tutorialModal`。

## 10. Markdown 渲染器（Markdown Renderer）

通用 Markdown 渲染组件，支持标题/代码/表格/公式，代码可复制下载。

**入口：** 被 AI 面板、README 阅读器等组件复用。

## 相关代码位置

| 模块 | 路径 |
|---|---|
| 批量颜色替换 | `src/addons/addons/batch-color-replace/` |
| 代码风格 | `src/addons/addons/coder-style/` |
| 注释同步 | `src/addons/addons/comment-vscode-sync/` |
| 语言包管理 | `src/addons/addons/language-package/`、`src/components/language-package/LanguagePackageManager.jsx` |
| 视频录制 | `src/addons/addons/mediarecorder/` |
| 自制积木增强 | `src/addons/addons/my-blocks-plus/` |
| 舞台相机 | `src/addons/addons/stage-camera/` |
| 视频弹窗 | `src/containers/video-modal.jsx` |
| 教程弹窗 | `src/containers/tutorial-modal.jsx` |
| Markdown 渲染器 | `src/components/markdown-renderer/markdown-renderer.jsx` |
