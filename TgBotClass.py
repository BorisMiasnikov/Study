import requests
import json
from TgBotConfig import keys, API_KEY


class ConvertionException(Exception):
    pass

class CashConverter:
    @staticmethod
    def get_price(quote: str, base: str, amount: str):

        if quote == base:
            raise ConvertionException(f'Не нужно переводить валюту {base} саму в себя.')
        try:
            quote_ticker = keys[quote]
        except KeyError:
            raise ConvertionException(f'Неудалось обработать валюту {quote},'
                                      f'вводите как указано в доступных валютах')

        try:
            base_ticker = keys[base]
        except KeyError:
            raise ConvertionException(f'Неудалось обработать валюту {base},'
                                      f'вводите как указано в доступных валютах')

        try:
            amount = float(amount)
        except ValueError:
            raise ConvertionException(f'Количество "{amount}" введено не верно,'
                                      f'вводить нужно цыфры, не целые числа разделять точкой.'
                                      f'Например 1.25, 0.37 и тд')

        r = requests.get(f'https://api.apilayer.com/fixer/latest?base={quote_ticker}&symbols={base_ticker}'
                         f'&apikey=' + API_KEY)
        total_base = json.loads(r.content)['rates'][base_ticker]
        return float(total_base)