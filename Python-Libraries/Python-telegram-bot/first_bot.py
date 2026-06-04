import os
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    name = update.effective_user.first_name
    
    # Use implicit string concatenation for better readability
    welcome_text = (
        f"درود {name} به پارس موبایل مرکزی خوش آمدید✅\n"
        "در این ربات میتوانید قیمت سراسری شعبات را مشاهده کنید💰\n"
        "برای مشاهده قیمت سراسری شعبات روی دکمه های زیر کلیک کنید👇"
    )
    await update.message.reply_text(welcome_text)

# Get the token from environment variables instead of hardcoding it
TOKEN = os.getenv("TELEGRAM_BOT_TOKEN", "YOUR_FALLBACK_TOKEN")
app = Application.builder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.run_polling()