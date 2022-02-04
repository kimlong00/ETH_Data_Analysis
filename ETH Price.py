import requests
import time
from datetime import datetime

ETH_API_URL = 'https://api.coingecko.com/api/v3/simple/price?ids=ethereum&vs_currencies=usd&include_market_cap=true&include_24hr_vol=true&include_24hr_change=true&include_last_updated_at=true'

def get_current_eth_price():
    response = requests.get(ETH_API_URL)
    data_list = response.json()
    eth_price = data_list['ethereum']['usd']
    print(eth_price)
    return eth_price

price_history = []
count = 0

while True:
    count += 1
    price = get_current_eth_price()
    date = datetime.now()
    price_history.append({'date': date, 'price': price})
    time.sleep(5)
    if count % 2 == 0:
        quit = int(input('Do you want to stop? (1/0): '))
        if quit:
            break
    
print(price_history)