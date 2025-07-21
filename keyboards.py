from telegram import ReplyKeyboardMarkup

def main_menu():
    menu = [
        ["🟩 Yer uchastkasi olish", "🟦 Yer uchastkasi ijaraga olish"],
        ["📝 Yer uchastkasi e'lon berish"],
        ["🏢 Kvartira olish", "🏠 Kvartira ijaraga olish"],
        ["📝 Kvartira/Ofis e'lon berish"],
        ["⭐️ VIP / Super VIP qilish"],
        ["📋 Mening e'lonlarim", "👤 Mening hisobim"],
        ["💳 Hisobni to‘ldirish", "🔔 Mening bildirishnomalarim"],
        ["🔎 So‘nggi e’lonlar", "📍 Mening qidiruvim"],
        ["📊 Bozor narxlari tahlili", "👥 Agentlar bo‘limi"],
        ["🆘 Yordam / FAQ", "📜 E’lon qoidalari"]
    ]
    return ReplyKeyboardMarkup(menu, resize_keyboard=True)
