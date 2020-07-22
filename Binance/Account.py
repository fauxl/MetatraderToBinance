import  flask
from flask import Flask, jsonify, render_template, session, request
from pymysql.constants.FIELD_TYPE import JSON
import json
from json import  JSONEncoder

class Account:
    id = ""
    name = ""
    balance = 0.0
    def __init__(self, id=" ", name=" ",balance = 0.0):

        self.id = id
        self.name = name
        self.balance = balance

    def PrintAccount(self):
        print("Numero Conto: "+self.id+ " Name: " +self.name+ " Balance: " +str(self.balance))


# subclass JSONEncoder
class SignalEncoder(JSONEncoder):
        def default(self, o):
            return o.__dict__
