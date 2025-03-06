import os
import json
from flask import Flask
#from flask_sqlalchemy import SQLAlchemy
from ollama import Client

app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))

@app.route('/<var>')
def home(var):
    return var

import routes

def getApp():
    return app

if __name__ == "__main__":
    app.run(debug=True, use_reloader=True)
