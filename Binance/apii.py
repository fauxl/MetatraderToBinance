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

conn = mysql.connect()
cursor =conn.cursor()

@app.route('/getdata')
def GetPositions():
    try:
        sql = ("SELECT * FROM position")
        cursor.execute(sql)
        res = cursor.fetchall()
        print(res)
        return jsonify(res)
    except TypeError as e:
        print(e)

def getOrder():
    Array = []
    sql = ("SELECT * FROM position")
    cursor.execute(sql)
    for row in cursor:
        ticket = row[0]
        typeop= row[1]
        typeop = 0
        if(str(row[1])=="SELL"):
            typeop= 1
        symbol=row[2]
        Orderop = row[3]
        SL = row[4]
        TP= row[5]
        close= row[6]
        stato = row[7]
        ord = Order(ticket,typeop,symbol,Orderop,SL,TP,close,stato)
        Array.append(ord)
    return Array


@app.route('/home', methods=['GET', 'POST'])
def addOrder():
    for t in GetData.read():
        found = "no"
        if getOrder() !=[]:
            for o in getOrder():
                if int(t.ticket) == int(o.ticket):
                    found = "yes"
                    stato = "Open"
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
                stato = "Open"
                sql = ("INSERT INTO position VALUES (%s, %s,%s, %s,%s, %s,%s,%s)")
                values = (ticket, typeop,symbol,SL,TP,Orderop,close,stato)
                cursor.execute(sql,values)
                conn.commit()
        if found == "yes":
                ticket = t.ticket
                SL = t.SL
                TP= t.TP
                close = t.close
                try:
                    sql1 = ("UPDATE position SET StopLoss=%s, TakeProfit=%s, CloseOperation=%s, Stato=%s where Ticket=%s")
                    values = (SL,TP,close,stato,ticket)
                    cursor.execute(sql1,values)
                    conn.commit()
                except TypeError as e:
                    print(e)
    return render_template("Home.html")





@app.route("/")
def index():
    BinanceApi.Object()
    return render_template("Home.html")

    """"
    render_template("index.html",
         mytitle=pagetitle,
                mycontent="Hello World")
    """

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=80, debug=True)