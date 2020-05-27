import  flask
from flask import Flask, jsonify, render_template, session, request
from pymysql.constants.FIELD_TYPE import JSON
import json
from json import  JSONEncoder

class Ticket:
    symbol = " "
    price = 0.0
    def __init__(self, symbol=" ", price=0.0):

        self.symbol = symbol
        self.price = price

    def PrintTicket(self):
        print("Simbolo: "+self.symbol+ " Price: " +str(self.typeop))


# subclass JSONEncoder
class TicketEncoder(JSONEncoder):
        def default(self, o):
            return o.__dict__
