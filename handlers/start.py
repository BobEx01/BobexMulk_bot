from telegram import Update
from telegram.ext import ContextTypes
from keyboards import main_menu

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    await update.message.reply_text(
        f"Assalomu alaykum, {user.first_name}!\n\n"
        "🏡 Bu Bobex Mulk Bot — Ko‘chmas mulk uchun platforma.\n"
        "Menyudan tanlang 👇",
        reply_markup=main_menu()
    )
