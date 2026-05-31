from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

TOKEN = "8744643110:AAEp76Yv6LsY9g2tplrHTyo83MN5dsJcMBU"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Bot ishladi 🚀")

app = Application.builder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))

print("Bot ishga tushdi...")
app.run_polling()
