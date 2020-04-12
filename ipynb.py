#!/usr/bin/env python
# coding: utf-8

# In[11]:


#get_ipython().system(' pip install python-telegram-bot')


# In[14]:
import vk
import time
import re
import telegram

session = vk.Session(access_token='c0a3e53715d1988940116e4a307e955bc09a513b6b2315c9645b0ab014f81203c7c34119f3e09600ad0fd')
vkapi = vk.API(session)

def make_post(text):
    print ("here")
    session = vk.Session(access_token='c0a3e53715d1988940116e4a307e955bc09a513b6b2315c9645b0ab014f81203c7c34119f3e09600ad0fd')
    vkapi = vk.API(session)
    vkapi.wall.post(message=text, v=5.8)

def sent_to_channel(text):
    bot = telegram.Bot("1074917414:AAGrV8VxNP38EQImKmhmq8jpKfNqh0SB7b0")
    bot.send_message(chat_id='-1001406885813', text=text)


from telegram.ext import Updater, CommandHandler, MessageHandler, Filters


def start(update, context):
    """Send a message when the command /start is issued."""
    update.message.reply_text('Hi!')


def help(update, context):
    """Send a message when the command /help is issued."""
    update.message.reply_text('Help!')


def echo(update, context):
    """Echo the user message."""
    #print ("123")
    print(update.message.text)
    update.message.reply_text("post is done")
    make_post(update.message.text)
    sent_to_channel(update.message.text)
    #update.message.reply_text("post is done")
    #print(stats)


def error(update, context):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, context.error)


def main():
    """Start the bot."""
    updater = Updater("1074917414:AAGrV8VxNP38EQImKmhmq8jpKfNqh0SB7b0",
                      request_kwargs={'proxy_url': 'socks5://51.83.2.136:1080'},
                      use_context=True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help))
    dp.add_handler(MessageHandler(Filters.text, echo))
    dp.add_error_handler(error)

    updater.start_polling()
    updater.idle()


# In[15]:


main()


# In[ ]:




