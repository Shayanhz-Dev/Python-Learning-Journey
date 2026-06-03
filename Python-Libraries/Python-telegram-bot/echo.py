import os
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes, MessageHandler, filters

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Send a welcome message when the /start command is issued."""
    name = update.effective_user.first_name
    
    # Use implicit string concatenation for better readability
    welcome_text = (
        f"درود {name} به پارس موبایل مرکزی خوش آمدید✅\n"
        "در این ربات میتوانید قیمت سراسری شعبات را مشاهده کنید💰\n"
        "برای مشاهده قیمت سراسری شعبات روی دکمه های زیر کلیک کنید👇"
    )
    await update.message.reply_text(welcome_text)

async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Echo the user message."""
    await update.message.reply_text(update.message.text)

# Retrieve the token securely from environment variables
TOKEN = os.getenv("TELEGRAM_BOT_TOKEN", "YOUR_TOKEN_HERE")
app = Application.builder().token(TOKEN).build()

# Register the command and message handlers
app.add_handler(CommandHandler("start", start))

# Use ~filters.COMMAND to prevent the bot from echoing commands like /start
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))

# Start the bot
app.run_polling()
