from configuration import VK_TOKEN, BOT_TOKEN, PROXY, CHAT_ID
import vk
import time
import re
import telegram
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

def make_post(text):
    session = vk.Session(access_token=VK_TOKEN)
    vkapi = vk.API(session)
    vkapi.wall.post(message=text, v=5.8)

def sent_to_channel(text):
    bot = telegram.Bot(BOT_TOKEN)
    bot.send_message(chat_id=CHAT_ID, text=text)

def start(update, context):
    update.message.reply_text('Привет! Я бот, с помощью которого ты сможешь опубиковать пост на странице Вконтакте и в телеграм-чате. Просто отправь мне текст поста! :)')

def help(update, context):
    update.message.reply_text('Для публикации поста просто отправь мне сообщение! :)')

def echo(update, context):
    make_post(update.message.text)
    sent_to_channel(update.message.text)
    update.message.reply_text("Сделано!")

def error(update, context):
    logger.warning('Update "%s" caused error "%s"', update, context.error)

def main():
    updater = Updater(BOT_TOKEN,
                      request_kwargs={'proxy_url': PROXY},
                      use_context=True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help))
    dp.add_handler(MessageHandler(Filters.text, echo))
    dp.add_error_handler(error)

    updater.start_polling()
    updater.idle()

main()

