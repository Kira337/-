import telebot

bot = telebot.TeleBot("7624948282:AAFDTQtwi8LZJ9bCd-t2EwnAAD8sNlz0zEg")


@bot.message_handler(commands=["start"])
def start_command(message):
    bot.send_message(message.chat.id, 'Приветствую! чтобы узнать о статистике загрезнения стран отправте /stat)


bot.message_handler(commands=["stat"])
def start_command(message):
    bot.send_message(message.chat.id,  
    '''Китай — 12 667,43 млн тонн выбросов CO₂
    США — 4 853,78 млн тонн
    Индия — 2 693,03 млн тонн
    Россия — 1 909,04 млн тонн
    Япония — 1 082,65 млн тонн
    Индонезия — 692,24 млн тонн
    Иран — 686,42 млн тонн
    Германия — 673,6 млн тонн
    Южная Корея — 635,5 млн тонн
    Саудовская Аравия — 607,91 млн тонн''')

bot.infinity_polling()


