from requests import Request, Session
import json
import pprint

url="https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest"
currencies=["BTC","ETH","BNB","SOL","AVAX","APE","ICP","FTT","MATIC","NEAR","DOT","LTC","SYNR","CFG","CLV","PLD","TEX","RAY","SRM","RACA","BLOK","ROCO","CWAR","AXS","SXP","CSPR","MINA","SOLPAD","ATLAS","SIDUS","CAKE","KSM","ALGO"]



print("SYMBOL              PRICE                   24H CHANGE       MARKETCAP")
for i in range(len(currencies)):
    parameters = {
        'symbol':currencies[i],
        'convert':'USD'
    }

    headers = {
        'Accepts':'application/json',
        'X-CMC_PRO_API_KEY':'XXXXXXX-XXXX-4cdd-XXXX-42XXXXXXX5d8e'
    }

    session = Session()
    session.headers.update(headers)

    response = session.get(url, params=parameters)
    shrt=json.loads(response.text)
    
    print(shrt['data'][parameters['symbol']]['name'],"   ",shrt['data'][parameters['symbol']]['quote']['USD']['price'],"     %",shrt['data'][parameters['symbol']]['quote']['USD']['percent_change_24h'],"     ",shrt['data'][parameters['symbol']]['quote']['USD']['market_cap'])

