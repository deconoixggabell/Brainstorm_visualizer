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

@app.route('/ideas/create', methods=['POST'])
def create_idea():
    if 'user_id' not in session:
        return redirect('/')

    if not Idea.validate_idea(request.form):
        return redirect('/new/visual')

    data = {
        'main_idea': request.form['main_idea'],
        'cat_i': request.form['cat_i'],
        'cat_ii': request.form['cat_ii'],
        'cat_iii': request.form['cat_iii'],
        'cat_iv': request.form['cat_iv'],
        'cat_v': request.form['cat_v'],
        'sub_c_i': request.form['sub_c_i'],
        'sub_c_ii': request.form['sub_c_ii'],
        'sub_c_iii': request.form['sub_c_iii'],
        'sub_c_iv': request.form['sub_c_iv'],
        'sub_c_v': request.form['sub_c_v'],
        'sub_c_vi': request.form['sub_c_vi'],
        'sub_c_vii': request.form['sub_c_vii'],
        'sub_c_viii': request.form['sub_c_viii'],
        'sub_c_ix': request.form['sub_c_ix'],
        'sub_c_x': request.form['sub_c_x'],
        'sub_c_xi': request.form['sub_c_xi'],
        'sub_c_xii': request.form['sub_c_xii'],
        'sub_c_xiii': request.form['sub_c_xiii'],
        'sub_c_xiv': request.form['sub_c_xiv'],
        'sub_c_xv': request.form['sub_c_xv'],
        'users_id': session['user_id']
    }

    Idea.create_idea(data)

    return redirect('/ideas')

@app.route('/ideas/<int:idea_id>')
def show_idea(idea_id):
    if 'user_id' not in session:
        return redirect('/')

    data = {
        'id': idea_id
    }

    idea = Idea.get_idea_with_user(data)

    return render_template('show_idea.html', idea=idea)

@app.route('/ideas/<int:idea_id>/edit')
def edit_idea(idea_id):
    if 'user_id' not in session:
        return redirect('/')

    data = {
        'id': idea_id
    }

    idea = Idea.get_idea_with_user(data)

    return render_template('edit_idea.html', idea=idea)

@app.route('/ideas/<int:idea_id>/update', methods=['POST'])
def update_idea(idea_id):
    if 'user_id' not in session:
        return redirect('/')

    if not Idea.validate_idea(request.form):
        return redirect(f'/ideas/{idea_id}/edit')

    data = {
        'id': idea_id,
        'main_idea': request.form['main_idea'],
        'cat_i': request.form['cat_i'],
        'cat_ii': request.form['cat_ii'],
        'cat_iii': request.form['cat_iii'],
        'cat_iv': request.form['cat_iv'],
        'cat_v': request.form['cat_v'],
        'sub_c_i': request.form['sub_c_i'],
        'sub_c_ii': request.form['sub_c_ii'],
        'sub_c_iii': request.form['sub_c_iii'],
        'sub_c_iv': request.form['sub_c_iv'],
        'sub_c_v': request.form['sub_c_v'],
        'sub_c_vi': request.form['sub_c_vi'],
        'sub_c_vii': request.form['sub_c_vii'],
        'sub_c_viii': request.form['sub_c_viii'],
        'sub_c_ix': request.form['sub_c_ix'],
        'sub_c_x': request.form['sub_c_x'],
        'sub_c_xi': request.form['sub_c_xi'],
        'sub_c_xii': request.form['sub_c_xii'],
        'sub_c_xiii': request.form['sub_c_xiii'],
        'sub_c_xiv': request.form['sub_c_xiv'],
        'sub_c_xv': request.form['sub_c_xv'],
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

    return redirect('/ideas')
