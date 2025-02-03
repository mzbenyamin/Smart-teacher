from telegram import Update
from telegram.ext import ContextTypes
from src.services.ai import get_ai_response

async def handle_text(update: Update, context: ContextTypes.DEFAULT_TYPE):
    response = await get_ai_response(update.message.text)
    await update.message.reply_text(response)
