from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import ephem
import datetime
TOKEN = "765226721:AAE1gFQ5H9odU9iZy0XuYjXQs14ttqiXz5I"
PROXY = {
    'proxy_url': 'socks5://t1.learn.python.ru:1080', 
    'urllib3_proxy_kwargs': {'username': 'learn', 'password': 'python'}}
# import logging
# logging.basicConfig(format='%(name)s - %(levelname)s - %(message)s',
#                     level=logging.INFO,
#                     filename='bot.log')

def greet_user(bot, update):
    text = 'Вызван /start'
    print(text)
    update.message.reply_text('Hello')
    # print(update) 

def talk_to_me(bot, update):
    user_text = update.message.text
    print(user_text)
    update.message.reply_text(user_text)

def find_planet(bot, update):
    d = datetime.datetime.now().strftime('%Y/%m/%d')
    planet = update.message.text.split()[1]
    update.message.reply_text(planet)
    if planet == 'Moon':
        moon = ephem.Moon(d)
        update.message.reply_text(ephem.constellation(moon))
    if planet == 'Mars':
        mars = ephem.Mars(d)
        update.message.reply_text(ephem.constellation(mars))
            


def main():
    mybot = Updater(TOKEN, request_kwargs=PROXY)
    dp = mybot.dispatcher
    dp.add_handler(CommandHandler('start', greet_user))
    dp.add_handler(CommandHandler('planet', find_planet))
    # dp.add_handler(MessageHandler(Filters.text, talk_to_me))
    mybot.start_polling()
    mybot.idle()
main()



#[Mercury, Venus, Earth, Mars]