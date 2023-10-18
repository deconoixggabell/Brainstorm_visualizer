from flask import *
import json, time
from flask import render_template, redirect, request, session, flash 
from flask_app import app
from flask_app.models.idea import Idea  
from flask_app.models.user import User

# working code in controllers users "Glory"


@app.route('/api', methods=['GET'])
def api():
    data_set = {
        'test': 'test',
        'message':'it worked yay',
        'timestamp': time.time()
    }
    result = json.dumps(data_set)
    return render_template("visual_code.html", result=result)