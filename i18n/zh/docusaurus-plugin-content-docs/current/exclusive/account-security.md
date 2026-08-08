---
title: 账号与安全
sidebar_position: 9
---

# 账号与安全

RemixWarp 提供了账号登录与 RemixWarp 社区接入相关的功能，这是 RemixWarp 中没有的。

## 1. RemixWarp 社区账号登录

RemixWarp/RemixWarp 账号登录弹窗，支持云同步、动态发布与编辑状态分享。

**功能：**
- 登录 RemixWarp/RemixWarp 账号
- 云同步设置
- 动态发布
- 编辑状态分享

**入口：** 菜单栏登录按钮弹出登录弹窗（`bilup-login-modal`）。

## 2. Rotur 会话与登录

通过 Rotur 会话接入社区平台，支持登录后发布项目、关注他人、跨设备同步设置。

## 3. 新手引导（Onboarding）

首次进入编辑器时展示的分步新手引导教程覆盖层。

**功能：**
- 分步引导（上一步/下一步/关闭）
- 联动打开"设置/工具/AI/文件"菜单
- 首次进入时通过 localStorage `mw:has-seen-onboarding` 判断触发
- 监听 `show-onboarding` 事件可重播

**状态管理（reducer：onboarding）：**
- 状态：`{ visible, step }`
- 动作：`SHOW` / `HIDE` / `NEXT` / `PREV` / `SKIP_ONBOARDING`

## 4. 兼容性转换（TV/平台兼容性）

将项目转换为其他编辑器的兼容格式并下载。

**功能：**
- 通过 `window.__remixWarpMenuBarInstance.getCompatibilityIssues()` 获取兼容性问题
- 通过 `handleCompatibilitySave()` 保存转换结果

## 5. 关于窗口与免责声明

"关于 RemixWarp"信息弹窗，说明与 RemixWarp 的关系及免责声明。

## 相关代码位置

| 模块 | 路径 |
|---|---|
| 登录弹窗 | `src/components/menu-bar/bilup-login-modal.jsx` |
| Rotur 登录 | `src/components/mw-rotur-login-modal/rotur-login-modal.jsx` |
| Rotur 会话 | `src/containers/rotur-session.jsx` |
| 新手引导容器 | `src/containers/onboarding.jsx` |
| 新手引导 reducer | `src/reducers/onboarding.js` |
| 兼容性转换 | `src/components/tw-compatibility-modal/` |
| 关于窗口 | `src/components/mw-info-modal/info-window.jsx` |
