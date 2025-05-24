# Telegram 记账机器人

这是一个基于 python-telegram-bot 构建的 Telegram 群组记账机器人。

## 🚀 部署到 Railway

### 1. 上传到 GitHub

```bash
git init
git remote add origin https://github.com/YOUR_USERNAME/telegram-account-bot.git
git add .
git commit -m "first commit"
git push -u origin master
```

### 2. Railway 步骤

- 打开 [https://railway.app](https://railway.app)
- New Project → Deploy from GitHub repo
- 添加环境变量 `BOT_TOKEN`
- 部署完成！

## 📦 使用命令示例

- `/admin` 或 `/gm` 呼出管理员菜单
- `/set 2` 设置默认费率
- `/set abc9.5` 设置别名费率
- `/price 9.9` 设置全局价格
- `/add 8` 增加微调金额8分
- `w-1000` 微信扣费1000元
- `+1000/6.15` 汇率记账
- `设置汇率7.8` 设置汇率

更多功能开发中...
