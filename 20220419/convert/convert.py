# pip install currencyconverter
import requests
from bs4 import BeautifulSoup
from currency_converter import CurrencyConverter

cc = CurrencyConverter()
print(cc.currencies)

cc2 = CurrencyConverter('http://www.ecb.europa.eu/stats/eurofxref/eurofxref.zip')
print(cc2.convert(1, 'USD', 'KRW'))


def get_exchange_rate(target1, target2):
    headers = {
        'User-Agent': 'Mozilla/5.0',
        'Content-Type': 'text/html; charset=utf-8'
    }
    # 일반적인 브라우저를 이용하여 접속한 것처럼 보이게 헤더를 추가함
    response = requests.get('http://kr.investing.com/currencies/{}-{}'.format(target1, target2), headers=headers)
    content = BeautifulSoup(response.content, 'html.parser')
    containers = content.find('span', {'data-test': 'instrument-price-last'})
    print(containers.text)


get_exchange_rate('usd', 'krw')

