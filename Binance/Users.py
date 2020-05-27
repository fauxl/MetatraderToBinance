import  flask
from flask import Flask, jsonify, render_template, session, request
from pymysql.constants.FIELD_TYPE import JSON
import json
from json import  JSONEncoder

class Users:
    user = " "
    password = " "
    mail = ""
    def __init__(self, user=" ", password=" ",mail=" "):

        self.user = user
        self.password = password

    def PrintUser(self):
        print("utente: "+self.user+ " password: " +str(self.password))


# subclass JSONEncoder
class UserEncoder(JSONEncoder):
        def default(self, o):
            return o.__dict__
