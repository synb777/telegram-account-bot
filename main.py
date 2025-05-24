import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters
import os
import json
import re
import handlers.admin as admin_handler

# 设置日志
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

# 读取环境变量
BOT_TOKEN = os.getenv("BOT_TOKEN")

# 初始化数据文件
DATA_FILE = "data.json"
if not os.path.exists(DATA_FILE):
    with open(DATA_FILE, "w") as f:
        json.dump({"rate": {}, "price": {}}, f)

def load_data():
    with open(DATA_FILE, "r") as f:
        return json.load(f)

def save_data(data):
    with open(DATA_FILE, "w") as f:
        json.dump(data, f)

async def set_rate(update: Update, context: ContextTypes.DEFAULT_TYPE):
    args = context.args
    if not args:
        await update.message.reply_text("请输入费率，例如：/set 2 或 /set 别名 2.5")
        return

    data = load_data()
    if len(args) == 1:
        data["rate"]["default"] = float(args[0])
        await update.message.reply_text(f"默认费率已设置为 {args[0]}")
    else:
        alias, rate = args[0], float(args[1])
        data["rate"][alias] = rate
        await update.message.reply_text(f"{alias} 的费率已设置为 {rate}")
    save_data(data)

async def set_price(update: Update, context: ContextTypes.DEFAULT_TYPE):
    args = context.args
    if not args:
        await update.message.reply_text("请输入价格，例如：/price 9.8")
        return
    price = float(args[0])
    data = load_data()
    data["price"]["global"] = price
    save_data(data)
    await update.message.reply_text(f"全局价格已设置为 {price}")

async def record_payment(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text.strip()
    match = re.match(r"([a-zA-Z]*)([wzk]?)-?([0-9]+)", text)
    if match:
        custom, method, amount = match.groups()
        method = method or "global"
        amount = int(amount)

        data = load_data()
        rate = data["rate"].get(custom or "default", 0)
        price = data["price"].get("global", 0)

        response = f"记录成功：方式：{method.upper()}，金额：{amount}，费率：{rate}%，价格：{price}"
        await update.message.reply_text(response)
    else:
        await update.message.reply_text("未识别的格式，请使用 w-1000 或 abcw-1000 等格式")

if __name__ == '__main__':
    app = ApplicationBuilder().token(BOT_TOKEN).build()

    # 命令处理
    app.add_handler(CommandHandler("admin", admin_handler.admin_menu))
    app.add_handler(CommandHandler("gm", admin_handler.admin_menu))
    app.add_handler(CommandHandler("set", set_rate))
    app.add_handler(CommandHandler("price", set_price))

    # 文本记账处理（如 w-1000）
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, record_payment))

    print("Bot is running...")
    app.run_polling()