import logging
import settings
from telegram.ext import Updater, CommandHandler, CallbackContext, MessageHandler, Filters

logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)',
                    level=logging.INFO,
                    filename='bot.log')

def start_bot(update: Updater, context: CallbackContext):
    print(update)
    mytext = f"""Hello, {update.message.chat.first_name}.
    
    I have only /start command! =)"""
    update.message.reply_text(mytext)

def chat(update: Updater, context: CallbackContext):
    text = update.message.text
    logging.info(text)
    update.message.reply_text(text)

def main():
    updtr = Updater(settings.TOKEN_TELEGRAM)
    updtr.dispatcher.add_handler(CommandHandler("start", start_bot))
    updtr.dispatcher.add_handler(MessageHandler(Filters.text, chat))
    updtr.start_polling()
    updtr.idle()

if __name__ == '__main__':
    logging.info("Bot started!")
    main()