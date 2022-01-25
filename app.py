# let op dit bestand moet app.py heten
# je runt hem met ::::>>   flask run

from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():    
    return "de flask app commit twee"