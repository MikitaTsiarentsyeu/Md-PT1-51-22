import telebot
from urllib.request import urlopen
from bs4 import BeautifulSoup

bot = telebot.TeleBot('5563351756:AAFn_3By3WjBA18FXgh_MHZOwnhb5dwfG2s')

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, "hello there!")

@bot.message_handler(commands=['update'])
def update_message(message):
    html = urlopen('https://kurs.onliner.by/')
    soup = BeautifulSoup(html)
    tag_list = soup.find_all('p', {'class':'value'})
    buy = tag_list[0].text
    sell = tag_list[1].text

    bot.send_message(message.chat.id, buy + ", " + sell)

bot.polling()