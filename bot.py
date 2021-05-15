#!/usr/bin/env python
# -*- coding: utf-8 -*-
# pylint: disable=W0613, C0116
# type: ignore[union-attr]
# This program is dedicated to the public domain under the CC0 license.

"""
Bot creado para Anne Belen
"""
try:
    from PIL import Image
except ImportError:
    import Image
import pytesseract
import logging
import constants
import os
from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)

logger = logging.getLogger(__name__)


def start(update: Update, context: CallbackContext) -> None:
    """Envía un mensaje cuando el comando /start se emite."""
    name = update.message.from_user.first_name
    update.message.reply_text('🤖 Hola! '+name + constants.welcome_text)
    update.message.reply_text("𝘽𝙤𝙩 𝙥𝙖𝙧𝙖 𝙘𝙤𝙣𝙫𝙚𝙧𝙩𝙞𝙧 𝙙𝙚 𝙞𝙢𝙖𝙜𝙚𝙣 𝙖 𝙩𝙚𝙭𝙩𝙤 \n Si necesitas ayuda usa /Ayuda")

def help_command(update: Update, context: CallbackContext) -> None:
    update.message.reply_text("/start : para iniciar el bot")
    update.message.reply_text("/donar : Para colaborar con el creador")
    update.message.reply_text("o simplemente envíame una imagen para reconocer el texto de ella")

def donate(update: Update, context: CallbackContext) -> None:
    update.message.reply_text(constants.donate_text)


def convert_image(update: Update, context: CallbackContext) -> None:
    chat_id = update.message.chat_id
    try:
        file_id = update.message.photo[-1].get_file()
        img_name = str(chat_id)+'.jpg'
        file_id.download(img_name)
        extracted_sting = (pytesseract.image_to_string(Image.open(img_name)))
        if extracted_sting:
            update.message.reply_text(''+str(extracted_sting)+'\n\nImagen a texto generada', reply_to_message_id = update.message.message_id)
        else:
            update.message.reply_text(constants.no_text_found)
    
    except Exception as e:
        update.message.reply_text("Error Occured: `"+str(e)+"`")
    
    finally:
        try:
            os.remove(img_name)
        except Exception:
            pass

def reply_to_text_message(update: Update, context: CallbackContext) -> None:
    update.message.reply_text(constants.reply_to_text_message)

def main():
    """Iniciar el bot."""

    bot_token = os.environ.get("BOT_TOKEN", "1896312596:AAHJbA14eiLMZ1XwfEi9d4hlOXg4JLy7PZ0")
    updater = Updater(bot_token, use_context=True)


    dispatcher = updater.dispatcher


    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("ayuda", help_command))
    dispatcher.add_handler(CommandHandler("donar", donate))


    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, reply_to_text_message))
    dispatcher.add_handler(MessageHandler(Filters.photo & ~Filters.command, convert_image))

    
    updater.start_polling()

    updater.idle()


if __name__ == '__main__':
    main()
