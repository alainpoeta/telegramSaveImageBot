#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Simple Bot to download Telegram messages and images
# This program is dedicated to the public domain under the CC0 license.

"""
This Bot uses the Updater class to handle the bot.
First, a few handler functions are defined. Then, those functions are passed to
the Dispatcher and registered at their respective places.
Then, the bot is started and runs until we press Ctrl-C on the command line.
Usage:
Basic Echobot example, repeats messages.
Press Ctrl-C on the command line or send a signal to the process to stop the
bot.
"""

import urllib

from telegram import Updater
import logging

#from django.conf import settings
APITOKEN='201647174:AAGhGU9ysAh4i2X8FfbpElS6Rjn37pO3GnM'

# Enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO)

logger = logging.getLogger(__name__)

#help_text = urllib.quote_plus("/random - Random pic \n /randomvideo - Random video")
help_text = "/random - Random pic\n/randomvideo - Random video\n/caso - comando senza senso"


# Define a few command handlers. These usually take the two arguments bot and
# update. Error handlers also receive the raised TelegramError object in error.
def start(bot, update):
    bot.sendMessage(update.message.chat_id, text='Ciao, questo è il bot di Case in festa')


def help(bot, update):
    #bot.sendMessage(update.message.chat_id, text='Help!')
    bot.sendMessage(update.message.chat_id, text=help_text)


def randomvideo(bot, update):
    bot.sendMessage(update.message.chat_id, text='Maiale')


def random(bot, update):
    bot.sendMessage(update.message.chat_id, text='Maiale piccolo')


def caso(bot, update):
    bot.sendMessage(update.message.chat_id, text='Non comando')


def echo(bot, update):
    bot.sendMessage(update.message.chat_id, text=update.message.text)


def error(bot, update, error):
    logger.warn('Update "%s" caused error "%s"' % (update, error))


def main():
    # Create the EventHandler and pass it your bot's token.
    #updater = Updater(settings.APITOKEN)
    updater = Updater(APITOKEN)

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # on different commands - answer in Telegram
    dp.addTelegramCommandHandler("start", start)
    dp.addTelegramCommandHandler("help", help)
    dp.addTelegramCommandHandler("randomvideo", randomvideo)
    dp.addTelegramCommandHandler("random", random)
    dp.addTelegramCommandHandler("caso", caso)

    # on noncommand i.e message - echo the message on Telegram
    dp.addTelegramMessageHandler(echo)

    # log all errors
    dp.addErrorHandler(error)

    # Start the Bot
    updater.start_polling()

    # Run the bot until the you presses Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()

if __name__ == '__main__':
    main()