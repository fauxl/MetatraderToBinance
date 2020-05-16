from binance.client import Client
import GetData
client = Client('v0KV0jkGS4Ah28deG9jKPwpCPiA5Ku0PCfUz1mEGRLk4NX1ZhoyvtoFDH86t1bA3',
                'F9DRH0F9WG2XChs0yze8k6kEcE2wVfe2Pp1MIGDwMVVRBhI846e0v3K5kSkQtrM6')
def Object():
    print(GetData.read())
    # get market depth
    #depth = client.get_order_book(symbol='BNBBTC')
    #for t in GetData.read():
        # place a test market buy order, to place an actual order use the create_order function
           # if (t.ticket!= "Ticket"):
                #print(t.PrintOrder())

        #   order = client.create_test_order(
              #      symbol=t.symbol,
               #     side=t.typeop,
                 #   type = "STOP_LOSS",
                   # stopPrice = t.SL,
                #    newClientOrderId = t.ticket,
                #type=Client.ORDER_TYPE_MARKET,
                 #   quantity=100)

#print(order)

# get all symbol prices
#prices = client.get_all_tickers()
#print(prices)
