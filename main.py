from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

TOKEN = 8744643110:AAHtVbi3CcCP0LD5Vz3T6eaOTLHkgGbVNyE

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("BoHasmi bot ishga tushdi!")

app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))

print("Bot ishlayapti...")
app.run_polling()
