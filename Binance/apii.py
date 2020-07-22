import  flask
from flask import Flask, jsonify, render_template, session, request
from pymysql.constants.FIELD_TYPE import JSON
#from flask_login import LoginManager
from flask import make_response, flash, session, redirect
from datetime import timedelta
from flask import *

import GetData
import BinanceApi
from functools import wraps
from flask import abort
from flaskext.mysql import MySQL
from Order import Order
from Users import Users
from argparse import ArgumentParser


app = Flask(__name__)

app.secret_key = 'many random bytes'

mysql = MySQL()

app.config['MYSQL_DATABASE_USER'] = 'Fauxl'
app.config['MYSQL_DATABASE_PASSWORD'] = ''
app.config['MYSQL_DATABASE_DB'] = 'positions'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'

mysql.init_app(app)


def logged(func):
    @wraps(func)
    def wrapper():
        name = request.cookies.get('userID')
        if (name == None):
            return redirect('/home')
        else:
            return func()
    return wrapper


@app.route('/login', methods=['GET', 'POST'])
def login():
    resp = render_template("login.html")
    if request.method == 'POST':
        username = request.form.get("username")
        password = request.form.get("password")
        print(username,password)
        max_age = timedelta(minutes=120)
        for i in LoginForm():
            print(i.PrintUser())
            if str(i.user) == str(username) and str(i.password) == str(password):
                resp = flask.make_response(redirect('/home'))
                resp.set_cookie('userID', i.user, max_age)

                return resp
        else:
            flask.flash('The username or password you entered are not correct')
            return redirect('/login')
    return resp

def LoginForm():
    ArrayUser=[]
    try:
        sql = ("SELECT * FROM users")
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.execute(sql)
        for row in cursor:
            user = row[0]
            password = row[1]
            email = row[2]
            key = row[3]
            skey= row[4]
            ac = row[5]
            ab = row[6]
            an = row[7]
            user = Users(user, password, email,key,skey,ac,an,ab)
            ArrayUser.append(user)
        cursor.close()
        return ArrayUser
    except TypeError as e:
        print(e)



@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        asd = request.json
        sql = ("INSERT INTO users VALUES (%s, %s,%s,%s, %s,%s,%s, %s)")
        Account = GetData.readAccountInfo()
        values = (asd["username"], asd["password"],asd["email"],"","", Account.id, Account.balance, Account.name)
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.execute(sql, values)
        conn.commit()
    return render_template("login.html")


@app.route("/logout")
@logged
def logout():
    #session['logged_in'] = False
    resp = make_response(render_template('home.html'))
    resp.set_cookie('userID', expires=0)
    return resp


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
        print(jsonify(res))
    except TypeError as e:
        print(e)

def getOrder():
    Array = []
    sql = ("SELECT * FROM position")
    conn = mysql.connect()
    cursor = conn.cursor()
    cursor.execute(sql)
    for row in cursor:
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
    return "lol"

def WriteOrder(symbol, tp, sl,volume,tipo):
    f = open("C:/Users/FauxL/AppData/Roaming/MetaQuotes/Terminal/2E8DC23981084565FA3E19C061F586B2/MQL4/Files/WriteOrder.csv","w")
    f.truncate(0)
    print(symbol)
    f.write(symbol +";"+ tp +";"+sl +";"+ volume+";"+tipo)
    f.close()
    return True

@logged
@app.route('/home', methods=['GET', 'POST'])
def addOrder():
    if getOrder() != []:
        for i in getOrder():
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
                name = request.cookies.get('userID')
                print(name)
                sql = ("INSERT INTO position VALUES (%s, %s,%s, %s,%s, %s,%s,%s,%s,%s,%s)")
                values = (ticket, typeop,symbol,SL,TP,Orderop,close,stato,quantity,profit,"FauxL")
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


@app.route("/home")
def index():
    return render_template("Home.html")


@app.route("/history")
@logged
def history():
    return render_template("OrderHistory.html")

#@login_required
@app.route("/insert", methods=['GET', 'POST'])
@logged
def insert():
    print(GetData.readInfo())
    if request.method == 'POST':
        symbol = request.form.get("symbol")
        tp = request.form.get("tp")
        sl = request.form.get("sl")
        volume = request.form.get("volume")
        tipo = request.form.get("tipo")
        if WriteOrder(symbol, tp, sl,volume,tipo):
            flask.flash('Your order has been sent to Metatrader successfully, check if it is open on your account!')
            return redirect("/insert")
        else:
            flask.flash('There is a problem with your order!')
    return render_template("NewOrder.html")



@app.route("/getTicket", methods=['GET'])
def getTick():
    return jsonify(GetData.readInfo())


@app.route("/getSignals", methods=['GET'])
def getSignals():
    print(GetData.readSignal())
    return jsonify(GetData.readSignal())

@app.route("/copy",methods=['GET','POST'])
@logged
def copy():
    if request.method == 'POST':
        key = request.form.get("key")
        secrete = request.form.get("secrete")
        print(key, secrete)
        if(BinanceApi.bconnection(key,secrete)):
            name = request.cookies.get('userID')
            sql1 = (
                "UPDATE users SET BinanceKey=%s, BinanceSKey=%s where user=%s")
            values = (key, secrete, name)
            conn = mysql.connect()
            cursor = conn.cursor()
            cursor.execute(sql1, values)
            conn.commit()
            cursor.close()
            flask.flash('Your binance account has successfully been inserted')
            redirect('/copy')
        else:
            flask.flash('The key you entered it\' s not corrected')
            redirect('/copy')
    return render_template("CopyTrading & Capture Signals.html")

@app.route("/signals", methods=['GET','POST'])
@logged
def signals():
    return render_template("Capture Signals.html")

@app.route("/data", methods=['GET', 'POST'])
@logged
def data():
    name = request.cookies.get('userID')
    balance = GetData.readAccountInfo()
    sql = ("UPDATE users SET AccountID=%s, AccountBalance=%s, AccountName=%s where user=%s")
    print(balance.PrintAccount())
    values = (balance.id, balance.balance, balance.name, name)
    conn = mysql.connect()
    cursor = conn.cursor()
    cursor.execute(sql, values)
    conn.commit()
    cursor.close()
    return render_template("Data.html")

@app.route("/getuserdata")
def getuserdata():
    name = request.cookies.get('userID')
    for i in LoginForm():
        if (i.user == name):
            return jsonify(i.__dict__)

@app.route("/close",methods=['GET', 'POST'])
def close():
    if request.method == 'POST':
        asd = request.json

    if Update(str(asd["code"]),str(-1),str(-1)):
       # flask.flash('Your request to close the order has been sent! ')
        return redirect("/home")

@app.route("/update",methods=['GET', 'POST'])
def update():
    if request.method == 'POST':
        asd = request.json

    if Update(str(asd["code"]),str(asd["sl"]),str(asd["tp"])):
        # flask.flash('Your request to close the order has been sent! ')
        return redirect("/home")

@app.route("/csignal",methods=['GET', 'POST'])
def csignal():
    if request.method == 'POST':
        asd = request.json

    if Update(str(asd["code"]),str(-2),str(-2)):
        # flask.flash('Your request to close the order has been sent! ')
        return redirect("/home")

def Update(code, tp, sl):
    f = open("C:/Users/FauxL/AppData/Roaming/MetaQuotes/Terminal/2E8DC23981084565FA3E19C061F586B2/MQL4/Files/Update.csv","w")
    f.truncate(0)
    print(code)
    f.write(code +";"+ tp +";"+sl +";")
    f.close()
    return True



    """"
    render_template("index.html",
         mytitle=pagetitle,
                mycontent="Hello World")
    """

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=80, debug=True)