from flask import Flask
from flask import render_template
from flask import jsonify
from flask import request
import pandas as pd
import datetime
import numpy as np

app = Flask(__name__)

def array_to_json(arr):
    return str(arr.tolist())

@app.route("/")
def hello_world():
    return render_template('generic.html')

if __name__ == '__main__':
    app.run()


