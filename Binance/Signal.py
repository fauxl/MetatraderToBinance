import  flask
from flask import Flask, jsonify, render_template, session, request
from pymysql.constants.FIELD_TYPE import JSON
import json
from json import  JSONEncoder

class Signal:
    id = ""
    pips = 0
    subs = 0
    name = " "
    currency = " "
    def __init__(self, id=" ", pips=0, subs = 0, name=" ", currency=" "):

        self.id = id
        self.pips = pips
        self.subs= subs
        self.name = name
        self.currency = currency

    def PrintTicket(self):
        print("Id Segnale: "+self.id+ " Pips: " +str(self.pips)+ " Subs: " +str(self.subs)
              + " Name: " +self.name + " Currency: " +self.currency)


# subclass JSONEncoder
class SignalEncoder(JSONEncoder):
        def default(self, o):
            return o.__dict__
