from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters
import handlers.admin
import os
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv("BOT_TOKEN")

app = ApplicationBuilder().token(TOKEN).build()

# 命令注册
app.add_handler(CommandHandler("admin", handlers.admin.admin_menu))
app.add_handler(CommandHandler("gm", handlers.admin.admin_menu))

print("Bot is running...")
app.run_polling()
