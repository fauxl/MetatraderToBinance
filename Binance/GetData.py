import fileinput as file
import array as arr
from Order import Order

def  read():
    count = 0
    separator =";"
    f = open("C:/Users/FauxL/AppData/Roaming/MetaQuotes/Terminal/2E8DC23981084565FA3E19C061F586B2/MQL4/Files/Register.csv","r")
    #text = f.readline()
    #result = text.split(separator)
    #print(result)
    n = f.readlines()

    count = sum(1 for _ in f)
    OrderArray = []

    for i in n:

        result = i.split(separator)
        ticket = result[1]
        if (ticket!= "Ticket"):
            typeop = result[2]
            """if  typeop == 1:
                typeop = "SELL"
            elif result[2] == 0:
                typeop = "BUY"
            elif result[2] == 2:
                typeop = "LIMIT_BUY"
            elif result[2] == 4:
                typeop = "LIMIT_SELL"
"""
            symbol = result[3]
            Orderop = result[4]
            SL = result[5]
            TP = result[6]
            close = result[7]
            stato = "Open"
            quantity = result[8]
            profit = result[9]
            order = Order(ticket,typeop,symbol,SL,TP,Orderop,close,stato,quantity,profit)
            #print(order.PrintOrder())
            OrderArray.append(order)
            #print("Ticket: "+ticket+ " Tipo: " +typeop + " Simbolo: " +symbol+
           # " PrezzoApertura: " + Orderopen + " PrezzoChiusura: " +close + " SL: "+SL+ " TP: "+TP)
            #print(order.PrintOrder())
    return OrderArray
