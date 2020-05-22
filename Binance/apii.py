import  flask
from flask import Flask, jsonify, render_template
from pymysql.constants.FIELD_TYPE import JSON

import GetData
import BinanceApi
from flaskext.mysql import MySQL
from Order import Order

app = Flask(__name__)
mysql = MySQL()

app.config['MYSQL_DATABASE_USER'] = 'Fauxl'
app.config['MYSQL_DATABASE_PASSWORD'] = ''
app.config['MYSQL_DATABASE_DB'] = 'positions'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'

mysql.init_app(app)

@app.route('/getdata')
def GetPositions():
    try:
        sql = ("SELECT * FROM position")
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.execute(sql)
        res = cursor.fetchall()
        cursor.close()
        return jsonify(res)
    except TypeError as e:
        print(e)

def getOrder():
    Array = []
    sql = ("SELECT * FROM position")
    conn = mysql.connect()
    cursor = conn.cursor()
    cursor.execute(sql)
    for row in cursor:
        print(row)
        ticket = row[0]
        typeop= row[1]
        typeop = 0
        if(str(row[1])=="SELL"):
            typeop= 1
        symbol=row[2]
        Orderop = row[5]
        SL = row[3]
        TP= row[4]
        close= row[6]
        stato = row[7]
        quantity=row[8]
        profit = row[9]
        print(ticket,typeop,symbol,SL,TP,Orderop,close,stato,quantity,profit);
        ord = Order(ticket,typeop,symbol,SL,TP,Orderop,close,stato,quantity,profit)
        Array.append(ord)
    cursor.close()
    return Array

def modifyOrder(t):
    ticket = t.ticket
    SL = t.SL
    TP = t.TP
    close = t.close
    profit = t.profit
    quantity = t.quantity
    stato = t.stato
    print(str(SL)+ " " +str(TP))
    try:
        sql1 = ("UPDATE position SET StopLoss=%s, TakeProfit=%s, CloseOperation=%s, Profit=%s, Quantity=%s, Stato=%s where Ticket=%s")
        values = (SL, TP, close, profit,quantity, stato, ticket)
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.execute(sql1, values)
        conn.commit()
        cursor.close()
    except TypeError as e:
        print(e)

def RetrieveInfo():
    



@app.route('/home', methods=['GET', 'POST'])
def addOrder():
    RetrieveInfo();
    if getOrder() != []:
        for i in getOrder():
            print(i.PrintOrder())
            for g in GetData.read():
                if int(i.ticket) == int(g.ticket):
                    i.stato = "Open"
                else:
                    i.stato = "Closed"
            modifyOrder(i)

    for t in GetData.read():
        found = "no"
        t.stato = "Open"
        if getOrder() !=[]:
            for o in getOrder():
                if int(t.ticket) == int(o.ticket):
                    found = "yes"
        if found == "no":
                ticket = t.ticket
                typeop = "BUY"
                if (int(t.typeop) == 1):
                    typeop = "SELL"
                symbol=t.symbol
                Orderop = t.Orderop
                SL = t.SL
                TP= t.TP
                close= t.close
                stato = t.stato
                profit = t.profit
                quantity = t.quantity
                #BinanceApi.Object(t)
                sql = ("INSERT INTO position VALUES (%s, %s,%s, %s,%s, %s,%s,%s,%s,%s)")
                values = (ticket, typeop,symbol,SL,TP,Orderop,close,stato,quantity,profit)
                conn = mysql.connect()
                cursor = conn.cursor()
                cursor.execute(sql,values)
                conn.commit()
                cursor.close()
        if found == "yes":
                modifyOrder(t)
    return render_template("Home.html")

@app.route('/getbinancedata')
def getOBinance():
    ArrayOrder = BinanceApi.GetBinanceOrder()
    return ArrayOrder


@app.route("/")
def index():
    return render_template("Home.html")

@app.route("/login")
def login():
    return render_template("Login.html")

@app.route("/history")
def history():
    return render_template("OrderHistory.html")

@app.route("/insert")
def insert():
    return render_template("NewOrder.html")

@app.route("/copy")
def copy():
    return render_template("CopyTrading & Capture Signals.html")

    """"
    render_template("index.html",
         mytitle=pagetitle,
                mycontent="Hello World")
    """

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=80, debug=True)