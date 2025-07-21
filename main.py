from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, MessageHandler, filters

TOKEN = '8133568549:AAFcJnEVsjduQ5uOFj5InvjEBELHSKjZNUo'

# Start komandasi
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    menu = [["🏠 E’lon joylash"], ["🔎 Qidirish"], ["👤 Mening e’lonlarim"], ["📈 Statistika", "⚙️ Sozlamalar"]]
    reply_markup = ReplyKeyboardMarkup(menu, resize_keyboard=True)

    await update.message.reply_text(
        f"Assalomu alaykum, {user.first_name}!\n\n"
        "🏡 Bu yerda siz uy, yer, kvartira yoki ofis sotish va ijaraga berish e’lonlarini joylashtirishingiz mumkin.\n\n"
        "Quyidagi menyudan birini tanlang 👇",
        reply_markup=reply_markup
    )

# Basic echo (keyin funksiyalar qo‘shiladi)
async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Iltimos, menyudan birini tanlang.")

def main():
    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))

    print("Bobex Mulk Bot ishga tushdi...")
    app.run_polling()

if __name__ == '__main__':
    main()
