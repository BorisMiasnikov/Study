from TgBotClass import ConvertionException, CashConverter
import telebot
from TgBotConfig import TOKEN, keys

''' Запрос возвращает результат такого вида 
https://api.apilayer.com/fixer/latest?base=USD&symbols=EUR,GBP&apikey=tLAJ4w1AfKPT5akpoT4UBCOmHVeh4G4i
{'success': True, 
'timestamp': 1703434563, 
'base': 'USD', 
'date': '2023-12-24', 
'rates': {'EUR': 0.90705, 'RUB': 92.125038}}'''
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start', 'help'])
def help(message: telebot.types.Message):
    text = ('Чтобы начать работу, введите команду боту в следующем формате:'
            '<имя валюты> <в какую валюту перевести> <количество переводимой валюты>\n'
            'Пример: Доллар Рубль 2. \n'
            'Доступные для перевода валюты: /values')
    bot.reply_to(message,text)

@bot.message_handler(commands=['values'])
def values(message: telebot.types.Message):
    text = 'Доступные валюты:'
    for key in keys.keys():
        text = '\n'.join((text,key,))
    bot.reply_to(message,text)

@bot.message_handler(content_types=['text',])
def convert(massage: telebot.types.Message):
    try:
        values = massage.text.split(' ')

        if len(values) != 3:
            raise ConvertionException('Неверное количество параметров.')

        quote, base, amount = values
        total_base = CashConverter.get_price(quote, base, amount)
    except ConvertionException as e:
        bot.reply_to(massage, f'Ошибка пользавателя.\n{e}')
    except Exception as e:
        bot.reply_to(massage, f'Не удалось обработать команду\n{e}')

    else:
        text = f'Цена {amount} {quote} в {base} - {total_base*float(amount)}'
        bot.send_message(massage.chat.id, text)

bot.polling(none_stop=True)



