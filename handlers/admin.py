from telegram import Update
from telegram.ext import ContextTypes

async def admin_menu(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "📋 管理员菜单：\n"
        "1️⃣ 设置费率: /set 2 或 /set 名称9.5\n"
        "2️⃣ 设置价格: /price 9.9 /pricez 9.8 /pricew /pricek\n"
        "3️⃣ 查询价格: /lz /lw /lk\n"
        "4️⃣ 微调金额: /add 8 /del 8\n"
        "5️⃣ 记账/扣费: +500 / w-1000 / abcw-1000\n"
        "6️⃣ 设置汇率: 设置汇率7.8 / 设置费率8%\n"
        "7️⃣ USD记账: 下发1000u / -1000u\n"
        "8️⃣ 回复记账、图文记账、转发记账等功能\n"
        "📌 更多功能开发中..."
    )
