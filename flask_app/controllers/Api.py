from flask import *
from flask_app import app
import json, time

@app.rounte('/', methods=['GET'])
def api():
    data_set = {
        'test': 'test',
        'message':'it worked yay',
        'timestamp': time.time()
    }
    result = json.dumps(data_set)
    return result