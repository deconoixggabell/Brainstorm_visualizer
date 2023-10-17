from flask import render_template, redirect, request, session, flash
from flask_app import app
from flask_app.models.user import User
from flask_app.models.idea import Idea
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)

@app.route('/')
def index():
    return redirect('/login')

@app.route('/login')
def sign_in():
    return render_template('login_and_registration.html' )

@app.route('/users/dashboard')
def show_dashboard():
    if "user_id" not in session:
        return redirect("/")
    if "logged_in" in session:
        if session['logged_in']:
            pass # TO DO  need to add the appropriate methods for the dashboard **************************************************************************************************
            # one_user_with_all_buyers = user.User.get_one_user_by_id_with_all_buyers(session['user_id'])
            # return render_template("all_buyers_dashboard.html", one_user_with_all_buyers=one_user_with_all_buyers)
    return redirect("/users/logout")

# Update Users Controller


# Delete Users Controller

@app.route('/users/delete/<int:user_id>', methods=['POST'])
def delete_user(user_id):
    if "user_id" not in session:
        return redirect("/")
    user.User.delete_user(user_id)
    return redirect('/users/logout')




