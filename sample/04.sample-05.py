from locale import currency
from currency_converter import CurrencyConverter
from bs4 import BeautifulSoup, BeautifulStoneSoup
from matplotlib import container
from requests import request
import requests
import requests
from sympy import content
cc = CurrencyConverter('http://www.ecb.europa.eu/stats/eurofxref/eurofxref.zip')
print(cc.convert(1,'USD','KRW'))

def get_exchange_rate(target1,target2):
    headers = {
        'User-Agent': 'Mozilla/5.0',
        'Content-Type' : 'text/html',
        'charset':'utf-8'
    }
    response = requests.get('https://kr.investing.com/currencies/{}-{}'.format(target1,target2),headers = headers)
    
    content = BeautifulSoup(response.content,'html.parser')
    containers = content.find('span',{'data-test':'instrument-price-last'})    
    print(containers)
    
get_exchange_rate('usd','krw')