# let op dit bestand moet app.py heten
# je runt hem met ::::>>   flask run

from flask import Flask
from lossefuncties import *

app = Flask(__name__)

@app.route("/")
def index():
    print( eenmethodevanmij() )    
    return "de flask app commit twee"