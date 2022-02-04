import requests

responses = requests.get('https://api.etherscan.io/api?module=account&action=balance&address=0x73a213df0f967dcb6b9dde0cb2462c128d3fc580&tag=latest&apikey=ICIMT7Y6Z5QSHHPCA27IU45ZIUXDC52T43')
data_list = responses.json()
eth_balance = int(data_list['result'])
eth_balance = eth_balance / 10**18
print(eth_balance, 'ETH')