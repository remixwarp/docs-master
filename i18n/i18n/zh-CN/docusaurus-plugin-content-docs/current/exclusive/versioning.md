---
title: 版本管理
sidebar_position: 11
---

# 版本管理

RemixWarp 提供了版本管理功能，这是 RemixWarp 中没有的。

## 1. 版本管理（Version Manager）

一个版本管理工具，用于检测应用更新并维护版本历史。

**功能：**
- 检测应用是否有更新（`checkForUpdate`）
- 维护版本历史记录
- 中文提交信息自动翻译
- 依赖实验性开关 `enableAutoUpdateCheck`

## 2. 更新日志弹窗（Update Log Modal）

展示版本更新记录的弹窗。

**功能：**
- 延迟 2 秒检查更新
- 从主题提取配色
- 翻译更新内容
- 关闭时标记版本为已查看（`markVersionAsSeen`）

## 3. 自定义默认角色（Custom Default Sprite）

将用户上传的默认角色持久化到 localStorage，加载默认项目时自动应用。

## 相关代码位置

| 模块 | 路径 |
|---|---|
| 版本管理 | `src/lib/version-manager.js` |
| 更新日志容器 | `src/containers/update-log-modal.jsx` |
| 自定义默认角色 | `src/lib/custom-default-sprite.js` |
