from flask_app import app
from flask import render_template, redirect, request, session, url_for, flash
from flask_app.models import user, idea # import entire file, rather than class, to avoid circular imports (separate with commas)
from flask_app.config.mysqlconnection import connectToMySQL
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)

# Create Users Controller

@app.route('/users/register', methods=["POST"])
def create_user():
    if request.form["which_form"] == "register":
        if not user.User.register_user(request.form):
            flash("Unable to add user.", "error")
            return render_template("login_and_registration.html", first_name=request.form["first_name"], last_name=request.form["last_name"], registration_email=request.form["email"] )

    return redirect("/users/dashboard") 

# Read Users Controller

@app.route('/')
def index():
    return render_template("login_and_registration.html")


@app.route('/users/dashboard')
def show_dashboard():
    if "user_id" not in session:
        return redirect("/")

    user_id = session['user_id']
    user_info = user.User.get_user_by_id(user_id)
    ideas = idea.Idea.read_all_ideas()
    # TO DO  need to add the appropriate methods for the dashboard **************************************************************************************************
    # one_user_with_all_buyers = user.User.get_one_user_by_id_with_all_buyers(session['user_id'])
    # return render_template("all_buyers_dashboard.html", one_user_with_all_buyers=one_user_with_all_buyers)
    return render_template("dashboard.html", user_info=user_info, ideas=ideas)


# Update Users Controller

@app.route('/users/edit_user_form/<int:user_id>')
def show_update_user_form(user_id):
    if "user_id" not in session:
        return redirect("/")
    if "logged_in" in session:
        if session['logged_in']:
            user_info = user.User.get_user_by_id(user_id)
            return render_template("user_edit.html", user_info=user_info)  
    return redirect("/users/logout") 

@app.route('/users/edit_profile/<int:user_id>', methods=['POST'])
def update_user_profile(user_id):

    if "user_id" not in session:
        return redirect("/")
    
    if request.form["which_form"] == "edit_profile":
        one_user = user.User.update_user_profile(request.form)

        if not one_user:
            flash("Unable to update user profile.", "error")
            path = f"/users/edit_user_form/{user_id}"    
            return redirect(path)

    return redirect('/users/dashboard')

@app.route('/users/update_password/<int:user_id>', methods=['POST'])
def update_user_password(user_id):

    if "user_id" not in session:
        return redirect("/")
    
    if request.form["which_form"] == "change_password":
        one_user = user.User.update_user_password(request.form)

        if not one_user:
            flash("Unable to update password.", "error")
            path = f"/users/edit_user_form/{user_id}"    
            return redirect(path)    
        
    return redirect('/users/dashboard')


# Delete Users Controller

@app.route('/users/delete/<int:user_id>', methods=['POST'])
def delete_user(user_id):
    if "user_id" not in session:
        return redirect("/")
    user.User.delete_user(user_id)
    return redirect('/users/logout')

# Login and Logout

@app.route('/users/logout')
def logout():
    #session.pop("user_id")
    session.clear()  
    return redirect("/")

@app.route('/users/login', methods=['POST'])
def login():

    if not user.User.login_user(request.form):
        return render_template("login_and_registration.html", login_email=request.form["email"])
    return redirect('/users/dashboard')
    

    
# api test
# just for testing will move to api file
from flask import *
from flask_app import app
from flask_app.controllers import users, ideas
import json, time

@app.route('/api', methods=['GET'])
def api():
    data_set = {
        'test': 'test',
        'message':'it worked yay',
        'timestamp': time.time()
    }
    result = json.dumps(data_set)
    return result
    return render_template("visual_code.html",)