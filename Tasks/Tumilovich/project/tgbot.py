import telebot
from telebot import types
from pycoingecko import CoinGeckoAPI
import time


cg = CoinGeckoAPI()

bot = telebot.TeleBot('5585583774:AAFChEh2kTqU3Szwi3N0C8NmaLGe5NlXbNQ')


@bot.message_handler(commands=['start'])

def main(message):
    button1 = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button1.add(types.KeyboardButton('Get crypto prices'), types.KeyboardButton('Track price target'))
    msg = bot.send_message(message.chat.id, 'choose options:', reply_markup=button1)
    bot.register_next_step_handler(msg, step)



def step(message):
    if message.text == 'Get crypto prices':
        step2(message)
    elif message.text == 'Track price target':
        step3(message)


def step2(message):

    button1 = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button1.add('Back to Main')
    crypto_list = ['bitcoin', 'ethereum', 'binancecoin', 'dogecoin', 'solana']
    price = cg.get_price(ids=crypto_list, vs_currencies='usd')

    for i in range(len(crypto_list)):
        show_user = f"{crypto_list[i].capitalize()} = {price[crypto_list[i]]['usd']}$"
        bot.send_message(message.chat.id, show_user, reply_markup=button1)
    go_main = bot.send_message(message.chat.id, 'Back to main?', reply_markup=button1)
    bot.register_next_step_handler(go_main, main)


def step3(message):
    button1 = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button1.add(types.KeyboardButton('BTC'), types.KeyboardButton('ETH'))
    msg = bot.send_message(message.chat.id, 'Please choose coin', reply_markup=button1)
    bot.register_next_step_handler(msg, step_target)


def step_target(message):
    crypto_dict = {'BTC':'bitcoin', 'ETH': 'ethereum'}
    coin = crypto_dict[message.text]
    markup = types.ReplyKeyboardRemove()
    msg = bot.send_message(message.chat.id, 'Please provide a target price', reply_markup=markup)
    bot.register_next_step_handler(msg, price_checker, coin)



def price_checker(message, coin):

    current_price = cg.get_price(ids=coin, vs_currencies='usd')[coin]['usd']
    bot.send_message(message.chat.id, f"You'll be notified when target price hit.\ncurrent : {coin.capitalize()} = {current_price}$")
    price = float(message.text)
    final_msg = f'You hit your target price!\nnow: {coin.capitalize()} = {current_price}$'
    if current_price > price:
        while True:
            current_price = cg.get_price(ids=coin, vs_currencies='usd')[coin]['usd']
            if current_price <= price :
                bot.send_message(message.chat.id, final_msg)
                break
            print('10sec passed')
            time.sleep(10)
            continue
    elif current_price == price:
        bot.send_message(message.chat.id, final_msg)
    elif current_price < price:
        while True:
            current_price = cg.get_price(ids='bitcoin', vs_currencies='usd')['bitcoin']['usd']
            if current_price >= price :
                bot.send_message(message.chat.id, final_msg)
                break
            print('10sec passed')
            time.sleep(10)
            continue


bot.polling(none_stop=True)