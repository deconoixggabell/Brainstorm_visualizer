from flask import flash
from flask_app.models import idea
from flask_bcrypt import Bcrypt
from flask_app.config.mysqlconnection import connectToMySQL
import re

db = "brainstorm_visualizer"
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class User:
    db = "brainstorm_visualizer"

    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.password = data['password']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.ideas = []

    @classmethod
    def create_user(cls, data):
        query = """INSERT INTO users (first_name, last_name, email, password)
        VALUES (%(first_name)s, %(last_name)s, %(email)s, %(password)s)"""
        user_id = connectToMySQL(cls.db).query_db(query, data)
        return user_id

    @classmethod
    def get_by_email(cls, data):
        query = "SELECT * FROM users WHERE email = %(email)s;"
        result = connectToMySQL(cls.db).query_db(query, data)
        if len(result) < 1:
            return False
        return cls(result[0])

    @classmethod
    def get_by_id(cls, user_id):
        query = "SELECT * FROM users WHERE id = %(id)s;"
        data = {
            'id': user_id
        }
        result = connectToMySQL(cls.db).query_db(query, data)

        if not result:
            return None

        return cls(result[0])

    @staticmethod
    def valid(user):
        is_valid = True
        if len(user['first_name']) < 2:
            flash("*First Name must be at least 1 character", category='registration_form_error')
            is_valid = False
        if len(user['last_name']) < 3:
            flash("*Last Name must be at least 3 characters", category='registration_form_error')
            is_valid = False

        query = "SELECT * FROM users WHERE email = %(email)s;"
        results = connectToMySQL(db).query_db(query, {'email': user['email']})

        if len(results) > 0:
            flash('Email already exists.', 'register_err')
            is_valid = False
        if len(user['email']) < 5:
            flash("*Email must be at least 5 characters", category='registration_form_error')
            is_valid = False
        if len(user['password']) < 8:
            flash("*Password must be at least 8 characters", category='registration_form_error')
            is_valid = False
        elif user['password'] != user['confirm_password']:
            flash("*Passwords do not match", category='registration_form_error')
            is_valid = False
        return is_valid

    @classmethod
    def get_user_with_ideas(cls, data):
        query = """
        SELECT * FROM users
        LEFT JOIN ideas ON users.id = ideas.users_id
        WHERE users.id = %(id)s
        """
        results = connectToMySQL(cls.db).query_db(query, data)

        user = cls(results[0])

        for row in results:
            idea_data = {
                'id': row['id'],
                'main_idea': row['main_idea'],
                'cat_i': row['cat_i'],
                'cat_ii': row['cat_ii'],
                'cat_iii': row['cat_iii'],
                'cat_iv': row['cat_iv'],
                'cat_v': row['cat_v'],
                'sub_c_i': row['sub_c_i'],
                'sub_c_ii': row['sub_c_ii'],
                'sub_c_iii': row['sub_c_iii'],
                'sub_c_iv': row['sub_c_iv'],
                'sub_c_v': row['sub_c_v'],
                'sub_c_vi': row['sub_c_vi'],
                'sub_c_vii': row['sub_c_vii'],
                'sub_c_viii': row['sub_c_viii'],
                'sub_c_ix': row['sub_c_ix'],
                'sub_c_x': row['sub_c_x'],
                'sub_c_xi': row['sub_c_xi'],
                'sub_c_xii': row['sub_c_xii'],
                'sub_c_xiii': row['sub_c_xiii'],
                'sub_c_xiv': row['sub_c_xiv'],
                'sub_c_xv': row['sub_c_xv'],
                'users_id': row['users_id'],
            }

            user.ideas.append(idea.Idea(idea_data))

        return user


