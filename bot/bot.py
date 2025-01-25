from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import Updater, CommandHandler, CallbackContext

# Replace this with your bot token from BotFather
BOT_TOKEN = "7778381944:AAFLORP8ZqODwdbXPmU2nM7Vn_3hHi8HGNE"

# Replace this with the hosted link to your web app
WEB_APP_URL = "https://vercel.com/merrys-projects-335617a5/merry_project"

def start(update: Update, context: CallbackContext):
    keyboard = [
        [InlineKeyboardButton("Open Web App", web_app=WEB_APP_URL)],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    update.message.reply_text("Click the button below to open the web app:", reply_markup=reply_markup)

def main():
    updater = Updater(BOT_TOKEN)
    dispatcher = updater.dispatcher
    dispatcher.add_handler(CommandHandler("start", start))
    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()
