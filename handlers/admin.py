from telegram import Update
from telegram.ext import ContextTypes

async def admin_menu(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = (
        "📋 管理员菜单：\n"
        "1. 设置费率 /set 或 /set 别名 费率\n"
        "2. 设置价格 /price 金额\n"
        "3. 记账：w-1000、abcw-1000\n"
        "4. 更多功能开发中..."
    )
    await update.message.reply_text(text)