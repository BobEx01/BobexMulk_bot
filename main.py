from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters
from config import TOKEN
from handlers.start import start
from keyboards import main_menu

async def handle_menu(update, context):
    text = update.message.text

    if text == "🟩 Yer uchastkasi olish":
        await update.message.reply_text("Yer uchastkasi olish bo‘limi...")
    
    elif text == "🟦 Yer uchastkasi ijaraga olish":
        await update.message.reply_text("Yer uchastkasi ijaraga olish bo‘limi...")

    elif text == "📝 Yer uchastkasi e'lon berish":
        await update.message.reply_text("Yer uchastkasi uchun e’lon joylash bo‘limi...")

    elif text == "🏢 Kvartira olish":
        await update.message.reply_text("Kvartira olish bo‘limi...")

    elif text == "🏠 Kvartira ijaraga olish":
        await update.message.reply_text("Kvartira ijaraga olish bo‘limi...")

    elif text == "📝 Kvartira/Ofis e'lon berish":
        await update.message.reply_text("Kvartira yoki Ofis uchun e’lon berish...")

    elif text == "⭐️ VIP / Super VIP qilish":
        await update.message.reply_text("VIP yoki Super VIP e’lon qilish uchun...")

    elif text == "📋 Mening e'lonlarim":
        await update.message.reply_text("Sizning joylagan e’lonlaringiz...")

    elif text == "👤 Mening hisobim":
        await update.message.reply_text("Profil va balans haqida ma’lumot...")

    elif text == "💳 Hisobni to‘ldirish":
        await update.message.reply_text("Hisobingizni to‘ldirish uchun...")

    elif text == "🔔 Mening bildirishnomalarim":
        await update.message.reply_text("Bildirishnomalaringiz...")

    elif text == "🔎 So‘nggi e’lonlar":
        await update.message.reply_text("So‘nggi joylangan e’lonlar...")

    elif text == "📍 Mening qidiruvim":
        await update.message.reply_text("Saqlangan qidiruvlaringiz...")

    elif text == "📊 Bozor narxlari tahlili":
        await update.message.reply_text("Viloyatlar kesimida o‘rtacha narxlar...")

    elif text == "👥 Agentlar bo‘limi":
        await update.message.reply_text("Agentliklar ro‘yxati...")

    elif text == "🆘 Yordam / FAQ":
        await update.message.reply_text("Yordam bo‘limi va tez-tez so‘raladigan savollar...")

    elif text == "📜 E’lon qoidalari":
        await update.message.reply_text("E’lon berish va foydalanish qoidalari...")

    else:
        await update.message.reply_text("Iltimos, menyudan birini tanlang.", reply_markup=main_menu())

def main():
    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_menu))

    print("Bobex Mulk Bot ishga tushdi...")
    app.run_polling()

if __name__ == '__main__':
    main()
