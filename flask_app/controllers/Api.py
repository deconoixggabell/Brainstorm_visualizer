from flask import *
import json, time
from flask import render_template, redirect, request, session, flash 
from flask_app import app
from flask_app.models.idea import Idea  

@app.route('/api/<int:id>', methods=['GET'])
def api(id):
    data ={
        'id' : id,
    }
    data_idea_sql = Idea.get_idea_with_user(data)
    data_idea_json = {
        'main_idea':data_idea_sql.main_idea,
        'cat_1': data_idea_sql.cat_1,
        'cat_2': data_idea_sql.cat_2,  
        'cat_3': data_idea_sql.cat_3,  
        'cat_4': data_idea_sql.cat_4,  
        'cat_5': data_idea_sql.cat_5,  
        'sub_c_1_1': data_idea_sql.sub_c_1_1,  
        'sub_c_1_2': data_idea_sql.sub_c_1_2,  
        'sub_c_1_3': data_idea_sql.sub_c_1_3,  
        'sub_c_2_1': data_idea_sql.sub_c_2_1,  
        'sub_c_2_2': data_idea_sql.sub_c_2_2,  
        'sub_c_2_3': data_idea_sql.sub_c_2_3,  
        'sub_c_3_1': data_idea_sql.sub_c_3_1,  
        'sub_c_3_2': data_idea_sql.sub_c_3_2,  
        'sub_c_3_3': data_idea_sql.sub_c_3_3, 
        'sub_c_4_1': data_idea_sql.sub_c_4_1,  
        'sub_c_4_2': data_idea_sql.sub_c_4_2,  
        'sub_c_4_3': data_idea_sql.sub_c_4_3,  
        'sub_c_5_1': data_idea_sql.sub_c_5_1,  
        'sub_c_5_2': data_idea_sql.sub_c_5_2,  
        'sub_c_5_3': data_idea_sql.sub_c_5_3,  
    }
    result = json.dumps(data_idea_json)
    # return render_template("visual_code.html",result =result )
    return (result)