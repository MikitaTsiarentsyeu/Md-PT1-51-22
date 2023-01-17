import telebot


token = '5918243391:AAEeFFVppa4WMhDgjoBxri5ULtnVPH9n0qk'
bot = telebot.TeleBot(token)


def start_message(message):
    bot.send_message(456361450, message)



   