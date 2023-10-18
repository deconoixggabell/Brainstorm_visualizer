from flask import render_template, redirect, request, session, flash 
from flask_app import app
from flask_app.models.idea import Idea  
from flask_app.models.user import User
from flask_bcrypt import Bcrypt
from flask_app.config.mysqlconnection import MySQLConnection

bcrypt = Bcrypt(app)

@app.route('/new/visual')
def add_visual():
    return render_template('visual_create.html')

@app.route('/create/visual', methods=['POST'])
def create_idea():
    if 'user_id' not in session:
        return redirect('/')

    data = {
        'main_idea': request.form['main_idea'],
        'cat_1': request.form.get('cat_1', ''),  # Use get() with a default value
        'cat_2': request.form.get('cat_2', ''),  # Use get() with a default value
        'cat_3': request.form.get('cat_3', ''),  # Use get() with a default value
        'cat_4': request.form.get('cat_4', ''),  # Use get() with a default value
        'cat_5': request.form.get('cat_5', ''),  # Use get() with a default value
        'sub_c_1_1': request.form.get('sub_c_1_1', ''),  # Use get() with a default value
        'sub_c_1_2': request.form.get('sub_c_1_2', ''),  # Use get() with a default value
        'sub_c_1_3': request.form.get('sub_c_1_3', ''),  # Use get() with a default value
        'sub_c_2_1': request.form.get('sub_c_2_1', ''),  # Use get() with a default value
        'sub_c_2_2': request.form.get('sub_c_2_2', ''),  # Use get() with a default value
        'sub_c_2_3': request.form.get('sub_c_2_3', ''),  # Use get() with a default value
        'sub_c_3_1': request.form.get('sub_c_3_1', ''),  # Use get() with a default value
        'sub_c_3_2': request.form.get('sub_c_3_2', ''),  # Use get() with a default value
        'sub_c_3_3': request.form.get('sub_c_3_3', ''),  # Use get() with a default value
        'sub_c_4_1': request.form.get('sub_c_4_1', ''),  # Use get() with a default value
        'sub_c_4_2': request.form.get('sub_c_4_2', ''),  # Use get() with a default value
        'sub_c_4_3': request.form.get('sub_c_4_3', ''),  # Use get() with a default value
        'sub_c_5_1': request.form.get('sub_c_5_1', ''),  # Use get() with a default value
        'sub_c_5_2': request.form.get('sub_c_5_2', ''),  # Use get() with a default value
        'sub_c_5_3': request.form.get('sub_c_5_3', ''),  # Use get() with a default value
        'users_id': session['user_id']
    }
    Idea.create_idea(data)

    return redirect('/users/dashboard')

@app.route('/ideas/<int:idea_id>')
def show_idea(idea_id):
    if 'user_id' not in session:
        return redirect('/')
    data = {
        'id': idea_id
    }
    idea = Idea.get_idea_with_user(data)

    return render_template('visual_view.html', idea=idea)


@app.route('/ideas/<int:idea_id>/edit')
def edit_idea(idea_id):
    if 'user_id' not in session:
        return redirect('/')

    data = {
        'id': idea_id
    }

    idea = Idea.get_idea_with_user(data)

    return render_template('visual_edit.html', idea=idea)

@app.route('/ideas/<int:idea_id>/update', methods=['POST'])
def update_idea(idea_id):
    if 'user_id' not in session:
        return redirect('/')

    if not Idea.validate_idea(request.form):
        return redirect(f'/ideas/{idea_id}/edit')

    data = {
        'main_idea': request.form['main_idea'],
        'cat_1': request.form.get('cat_1', ''),  # Use get() with a default value
        'cat_2': request.form.get('cat_2', ''),  # Use get() with a default value
        'cat_3': request.form.get('cat_3', ''),  # Use get() with a default value
        'cat_4': request.form.get('cat_4', ''),  # Use get() with a default value
        'cat_5': request.form.get('cat_5', ''),  # Use get() with a default value
        'sub_c_1_1': request.form.get('sub_c_1_1', ''),  # Use get() with a default value
        'sub_c_1_2': request.form.get('sub_c_1_2', ''),  # Use get() with a default value
        'sub_c_1_3': request.form.get('sub_c_1_3', ''),  # Use get() with a default value
        'sub_c_2_1': request.form.get('sub_c_2_1', ''),  # Use get() with a default value
        'sub_c_2_2': request.form.get('sub_c_2_2', ''),  # Use get() with a default value
        'sub_c_2_3': request.form.get('sub_c_2_3', ''),  # Use get() with a default value
        'sub_c_3_1': request.form.get('sub_c_3_1', ''),  # Use get() with a default value
        'sub_c_3_2': request.form.get('sub_c_3_2', ''),  # Use get() with a default value
        'sub_c_3_3': request.form.get('sub_c_3_3', ''),  # Use get() with a default value
        'sub_c_4_1': request.form.get('sub_c_4_1', ''),  # Use get() with a default value
        'sub_c_4_2': request.form.get('sub_c_4_2', ''),  # Use get() with a default value
        'sub_c_4_3': request.form.get('sub_c_4_3', ''),  # Use get() with a default value
        'sub_c_5_1': request.form.get('sub_c_5_1', ''),  # Use get() with a default value
        'sub_c_5_2': request.form.get('sub_c_5_2', ''),  # Use get() with a default value
        'sub_c_5_3': request.form.get('sub_c_5_3', ''),  # Use get() with a default value
        'users_id': session['user_id']
    }
    Idea.update_idea(data)

    return redirect('/ideas')

@app.route('/ideas/<int:idea_id>/delete')
def delete_idea(idea_id):
    if 'user_id' not in session:
        return redirect('/')

    data = {
        'id': idea_id
    }

    Idea.delete_idea(data)

    return redirect('/users/dashboard')
