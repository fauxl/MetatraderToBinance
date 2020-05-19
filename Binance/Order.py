class Order:
    ticket = 0.0
    typeop= 0
    symbol=""
    Orderop =0.0
    SL =0.0
    TP=0.0
    close=0.0
    stato=""
    quantity=0.0
    profit=0.0
    def __init__(self, ticket=0.0, typeop=0, symbol=" ",  SL=0, TP=0,Orderop=0.0, close=0.0, stato="",quantity=0.0, profit=0.0 ):
        self.ticket = ticket
        self.typeop = typeop
        self.symbol = symbol
        self.Orderop = Orderop
        self.SL = SL
        self.TP = TP
        self.close =close
        self.stato = stato
        self.quantity = quantity
        self.profit = profit

    def PrintOrder(self):
        print("Ticket: "+str(self.ticket)+ " Tipo: " +str(self.typeop)+ " Simbolo: " +self.symbol+
         " PrezzoApertura: " + str(self.Orderop) + " PrezzoChiusura: " +str(self.close) + " SL: "+str(self.SL)+ " TP: "+str(self.TP) + "Stato: " +self.stato
       + "Quantità: " + str(self.quantity) +" Profitto: "+str(self.profit))

