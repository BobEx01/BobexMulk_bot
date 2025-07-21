import logging
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters
from config import TOKEN
from handlers.start import start
from keyboards import main_menu

# Loglash konfiguratsiyasi
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

# Barcha menyu tugmalarini handler qilish
async def handle_menu(update, context):
    text = update.message.text

    mapping = {
        "🟩 Yer uchastkasi olish": "Yer uchastkasi olish bo‘limi...",
        "🟦 Yer uchastkasi ijaraga olish": "Yer uchastkasi ijaraga olish bo‘limi...",
        "📝 Yer uchastkasi e'lon berish": "Yer uchastkasi uchun e’lon joylash bo‘limi...",
        "🏢 Kvartira olish": "Kvartira olish bo‘limi...",
        "🏠 Kvartira ijaraga olish": "Kvartira ijaraga olish bo‘limi...",
        "📝 Kvartira/Ofis e'lon berish": "Kvartira yoki Ofis uchun e’lon berish...",
        "⭐️ VIP / Super VIP qilish": "VIP yoki Super VIP e’lon qilish uchun...",
        "📋 Mening e'lonlarim": "Sizning joylagan e’lonlaringiz...",
        "👤 Mening hisobim": "Profil va balans haqida ma’lumot...",
        "💳 Hisobni to‘ldirish": "Hisobingizni to‘ldirish uchun...",
        "🔔 Mening bildirishnomalarim": "Bildirishnomalaringiz...",
        "🔎 So‘nggi e’lonlar": "So‘nggi joylangan e’lonlar...",
        "📍 Mening qidiruvim": "Saqlangan qidiruvlaringiz...",
        "📊 Bozor narxlari tahlili": "Viloyatlar kesimida o‘rtacha narxlar...",
        "👥 Agentlar bo‘limi": "Agentliklar ro‘yxati...",
        "🆘 Yordam / FAQ": "Yordam bo‘limi va tez-tez so‘raladigan savollar...",
        "📜 E’lon qoidalari": "E’lon berish va foydalanish qoidalari..."
    }

    response = mapping.get(text, "Iltimos, menyudan birini tanlang.")
    await update.message.reply_text(response, reply_markup=main_menu())

def main():
    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_menu))

    logging.info("Bobex Mulk Bot Railway uchun ishga tushdi...")
    app.run_polling()

if __name__ == '__main__':
    main()
