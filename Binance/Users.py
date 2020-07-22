import  flask
from flask import Flask, jsonify, render_template, session, request
from pymysql.constants.FIELD_TYPE import JSON
import json
from json import  JSONEncoder

class Users:
    user = " "
    password = " "
    mail = ""
    key=""
    skey=""
    id = ""
    name = ""
    balance = 0.0
    def __init__(self, user=" ", password=" ",mail=" ",key=" ", skey="",id=" ", name=" ",balance = 0.0):

        self.user = user
        self.password = password
        self.mail = mail
        self.key = key
        self.skey = skey
        self.id = id
        self.name = name
        self.balance = balance

    def PrintUser(self):
        print("utente: "+self.user+ " password: " +self.password + "mail: "+self.user+ " key: " +self.key +" secrete jey: "+self.skey
              +" Numero Conto: "+str(self.id)+ " Name: " +str(self.name)+ " Balance: " +str(self.balance))


# subclass JSONEncoder
class UserEncoder(JSONEncoder):
        def default(self, o):
            return o.__dict__
