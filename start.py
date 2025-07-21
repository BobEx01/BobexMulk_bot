from telegram import Update
from telegram.ext import ContextTypes
from keyboards import main_menu

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    await update.message.reply_text(
        f"Assalomu alaykum, {user.first_name}!\n\n"
        "🏡 Bu Bobex Mulk Bot — Ko‘chmas mulk sotish, olish va ijaraga berish uchun qulay platforma.\n\n"
        "Menyudan kerakli bo‘limni tanlang 👇",
        reply_markup=main_menu()
    )
