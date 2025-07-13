import os
from dotenv import load_dotenv
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes

# Load environment variables
load_dotenv()
BOT_TOKEN = os.getenv("BOT_TOKEN")
AFFILIATE_TAG = os.getenv("AFFILIATE_TAG")

# Start command
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "👗 Welcome to *FashionUnder999Bot!*\n\n"
        "🛍️ Type anything like:\n"
        "`kurti under 300`\n"
        "`heels for party`\n"
        "`saree under 500`\n\n"
        "And I’ll send you the best Amazon affiliate deals instantly!\n\n"
        "💖 Save Money. Shop Smart. Support Women Entrepreneurs!",
        parse_mode='Markdown'
    )

# Search query handler
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_input = update.message.text.strip()
    if not user_input:
        await update.message.reply_text("Please type what you're looking for 😇")
        return

    query = user_input.replace(" ", "+")
    amazon_url = f"https://www.amazon.in/s?k={query}&tag={AFFILIATE_TAG}"

    reply = (
        f"🛍️ Here's what I found for *{user_input}*\n"
        f"👉 [Click here to view on Amazon]({amazon_url})\n\n"
        f"💖 *Powered by @FashionUnder999Bot* — India’s Budget Fashion Helper 👗"
    )
    await update.message.reply_text(reply, parse_mode='Markdown')

# Run the bot
if __name__ == '__main__':
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    print("🤖 Bot is running...")
    app.run_polling()
