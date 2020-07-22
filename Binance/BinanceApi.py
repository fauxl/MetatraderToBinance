import Order as order
from binance.client import Client
import binance
from binance.enums import *

import GetData
import apii
def bconnection(key,secrete):
    try:
        client =  Client(key,
                secrete)
        status = client.get_account_status()
        print(status)

        return True
    except KeyError:
        return False

def Object(t, client):
    #print(GetData.read())
    # get market depth
    #depth = client.get_order_book(symbol='BNBBTC')
        # place a test market buy order, to place an actual order use the create_order function
            order = client.create_test_order(
            symbol=t.symbol,
            side=t.typeop,
            type = "STOP_LOSS",
            stopPrice = t.SL,
            newClientOrderId = t.ticket,
            quantity=100)

def GetBinanceOrder():
    orders = client.get_all_orders()
    print(orders)


#print(order)

# get all symbol prices
#prices = client.get_all_tickers()
#print(prices)
