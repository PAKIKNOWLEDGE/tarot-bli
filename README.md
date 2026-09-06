# 幻星集塔罗 · PHANTASIA TAROT

基于 bilibili《幻星集塔罗》卡面插画制作的单页塔罗占卜应用。纯原生 HTML/CSS/JS，无构建、无依赖。

## 功能

- **全部 78 张牌均为官方插画**：22 张大阿尔卡纳 + 56 张小阿尔卡纳
  - 小阿尔卡纳采用《幻星集塔罗 II》全套官方卡面（ACE–X + 侍从/骑士/王后/国王，四花色各 14 张）
- **3 张赠送卡**：幻星集 II 纪念 / 魔法奇幻花园 / 新年发财，收录于牌库「赠送牌」分类，仅供观赏，不参与抽牌
- **4 种牌阵**：每日指引（1 牌）/ 时间之流（3 牌）/ 命运十字（5 牌）/ 凯尔特十字（10 牌），各带专属摆位布局
- **真随机**：Fisher–Yates 全牌洗切 + `crypto.getRandomValues` 无偏取整，逆位 50/50 密码学随机
- 正逆位解读、星之判词、占卜档案（localStorage）
- 全部牌浏览 + 按花色筛选 + 牌面详情

## 使用

直接双击 `index.html` 即可；或本地起服务：

```bash
python -m http.server 8642
# 访问 http://127.0.0.1:8642/
```

### iOS 单文件版

[`幻星集塔罗.html`](./幻星集塔罗.html) 为单文件版：27 张卡图压缩并 base64 内嵌（约 7 MB），无任何外部依赖，可直接发送（AirDrop/微信）到 iPhone/iPad 用 Safari 打开。

重新生成单文件版：

```bash
pip install pillow
python build_single.py
```

## 目录结构

```
index.html          主页面（引用 images/ 下的卡图）
images/             幻星集塔罗卡面插画（22 大 + 56 小 + 3 赠送 + 卡背）
build_single.py     单文件版打包脚本
幻星集塔罗.html      单文件版（构建产物，约 14 MB）
```

## 素材来源

- 大阿尔卡纳与初版花色图：[bilibili · 幻星集塔罗](https://www.bilibili.com/opus/441785769200577976)
- 小阿尔卡纳全套、赠送卡与新版卡背：[bilibili · 幻星集塔罗 II](https://www.bilibili.com/opus/537475591865428441)

卡面插画版权归原作者所有，此处仅作学习欣赏用途。
