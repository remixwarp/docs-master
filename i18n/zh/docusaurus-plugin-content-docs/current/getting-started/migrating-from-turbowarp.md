---
title: 从 TurboWarp 迁移
sidebar_position: 6
---

# 从 TurboWarp 迁移

RemixWarp 构建在 TurboWarp 之上，因此如果您已经在使用 TurboWarp，编辑器看起来和使用起来几乎完全相同。编译器、任意帧率、自定义舞台大小、插件、主题、还原点、打包器和高级设置都会保留，并按您的预期工作。项目使用相同的 `.sb3` 格式，TurboWarp 项目可以通过 **文件然后从电脑加载** 直接在 RemixWarp 中打开。

本页重点介绍 RemixWarp 在 TurboWarp 基础上新增的功能。

## 社区平台与 Rotur 账户

最大的新增功能是完整的社区平台。RemixWarp 编辑器和社区站点由同一个构建提供，因此发布、个人资料和浏览项目都集成在同一个应用中。

- 使用 **Rotur 账户**登录。在菜单栏中，您可以通过 **文件然后保存到 RemixWarp** 将项目直接保存到账户，然后打开其项目页面。
- 登录后，您会获得个人资料、通知和社交功能（关注、评论和发帖）。
- 登录状态下，您的设置和主题会在设备间同步。

构建、运行、打包或本地保存项目不需要账户，这与 TurboWarp 完全一致。账户只增加社区功能。请参阅[项目管理](/user-guide/project-management)。

## 额外积木与扩展

RemixWarp 包含超出 TurboWarp 的额外积木和扩展。请在[扩展概览](/extensions/overview)和[RemixWarp 额外积木](/user-guide/mistwarp-extras)中浏览。

## Git 版本控制

RemixWarp 可以用 **git** 跟踪项目。项目一旦存在仓库，文件菜单就会为远程仓库提供提交、推送和拉取操作，因此您可以通过 git 托管来管理版本并与他人协作。请参阅[Git](/user-guide/git)。

## 实时协作

RemixWarp 增加了实时协作：多人可以同时编辑同一个项目，并看到彼此在编辑器中的存在。请参阅[协作](/user-guide/collaboration)。

## 调试器

RemixWarp 包含一个调试器，用于检查运行中的项目、单步执行并观察状态，这超出了 TurboWarp 的标准工具。请参阅[调试器](/user-guide/debugger)。

## 主题与插件

TurboWarp 的插件和主题系统都存在并得到扩展。RemixWarp 提供自己的主题（包括自定义配色方案）和自己精选的插件。请参阅[主题](/user-guide/themes)和[插件](/user-guide/addons)。

## 相同之处

- 积木、编译器和运行时行为。请参阅[积木概览](/user-guide/overview)。
- 高级设置，如[自定义 FPS](/website/custom-fps)、[自定义舞台大小](/website/custom-stage-size)、[高质量画笔](/website/high-quality-pen)、[插值](/website/interpolation)和[移除限制](/website/remove-limits)。
- 用于构建项目独立版本的[打包器](/packager/overview)。
- URL 参数、嵌入和云变量。请参阅[URL 参数](/website/url-parameters)、[嵌入](/website/embedding)和[云变量](/website/cloud-variables)。

## 另请参阅

- [简介](/getting-started/introduction)
- [编辑器导览](/getting-started/editor-tour)
- [从 Scratch 迁移](/getting-started/migrating-from-scratch)
