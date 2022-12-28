from telegram.ext.updater import Updater
from telegram.update import Update
from telegram.ext.callbackcontext import CallbackContext
from telegram.ext.commandhandler import CommandHandler
from telegram.ext.messagehandler import MessageHandler
from telegram.ext.filters import Filters
from IPLocation import IPLocation
from TrataIPLocation import TrataIPLocation
import os

token = os.environ.get('tokem')
updater = Updater(token,
                  use_context=True)


def start(update: Update, context: CallbackContext):
    update.message.reply_text("Bem vindo ao bot!")


def unknown_text(update: Update, context: CallbackContext):
    text = update.message.text
    if TrataIPLocation.is_valid_input(text):
        ip = IPLocation()
        location = ip.fetch(text)
        trataiplocation = TrataIPLocation(location)
        update.message.reply_text(str(trataiplocation))
    else:
        update.message.reply_text("O texto enviado não é um endereço IP ou um domínio válido.")


updater.dispatcher.add_handler(CommandHandler('start', start))

# Filters out unknown messages.
updater.dispatcher.add_handler(MessageHandler(Filters.text, unknown_text))

updater.start_polling()
