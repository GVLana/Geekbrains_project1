from requests import get, utils
from decimal import Decimal
from datetime import date
from sys import argv


response = get('http://www.cbr.ru/scripts/XML_daily.asp')
encodings = utils.get_encoding_from_headers(response.headers)
content = response.content.decode(encoding=encodings).split('><Valute')
# print(content)


def currency_rate(x):
    d, m, y = map(int, content[0].split('"')[-4].split('.'))
    for i in content:
        if x.upper() in i:
            print(date(year=y, month=m, day=d))
            print(x.upper(), end=" ")
            # return float(i.replace('/', '').split('<Value>')[-2].replace(',', '.'))
            return Decimal(i.replace('/', '').split('<Value>')[-2].replace(',', '.'))


if __name__ == '__main__':
    keyword = argv[1]
    print(currency_rate(keyword))
