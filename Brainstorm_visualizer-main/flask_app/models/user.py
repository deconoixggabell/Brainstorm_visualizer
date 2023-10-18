from flask import flash
from flask_app import app
from flask import render_template, redirect, request, session, url_for, flash
from flask_app.models import idea
from flask_app.config.mysqlconnection import connectToMySQL
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)
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

    # Create Users Models

    @classmethod
    def create_user(cls, data):
        query = """INSERT INTO users (first_name, last_name, email, password)
        VALUES (%(first_name)s, %(last_name)s, %(email)s, %(password)s)"""
        user_id = connectToMySQL(cls.db).query_db(query, data)
        return user_id
    
    @classmethod
    def register_user(cls, user_data):
        if not cls.validate_user_registration(user_data):
            return False
        
        user_data = user_data.copy()  #immutable, so need to make a copy to add password

        user_data['password'] = bcrypt.generate_password_hash(user_data['password'])


        query = """
                INSERT INTO users(first_name, last_name, email, password) 
                VALUES (%(first_name)s, %(last_name)s, %(email)s, %(password)s);
        """
        
        user_id = connectToMySQL(cls.db).query_db(query, user_data)

        session['user_id'] = user_id
        session['first_name'] = user_data["first_name"]
        session['logged_in'] = True

        return True
    
    # Read Users Models

    @classmethod
    def get_by_email(cls, data):
        query = "SELECT * FROM users WHERE email = %(email)s;"
        result = connectToMySQL(cls.db).query_db(query, data)
        if len(result) < 1:
            return False
        return cls(result[0])
    
    @classmethod
    def get_user_by_id(cls, user_id):
        query = "SELECT * FROM users WHERE id = %(id)s;"
        data = {
            'id': user_id
        }
        result = connectToMySQL(cls.db).query_db(query, data)

        if not result:
            return None

        return cls(result[0])
    
    # the get_user_by_email method will be used when we need to retrieve just one specific row of the table
    @classmethod
    def get_user_by_email(cls, email):
        query = """
                SELECT * FROM users
                WHERE email = %(email)s;
        """
        data = {'email': email}
        result = connectToMySQL(cls.db).query_db(query, data)  # a list with one dictionary in it
        if len(result) < 1:     # no matching user
            return False
        one_user = cls(result[0])
        return one_user # returns user object
    
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
    
    # Update User Models
    
    @classmethod
    def update_user_password(cls, user_data):  

        user_data = user_data.copy()

        is_valid = cls.validate_user_password(user_data)
        
        if not is_valid:
            return False

        this_user = cls.get_user_by_id(user_data['id'])

        if session['user_id'] != this_user.id:
            return False
        
        user_data['password'] = bcrypt.generate_password_hash(user_data['password'])
    
        query = """
                UPDATE users
                SET password = %(password)s
                WHERE id=%(id)s;    
                """
        connectToMySQL(cls.db).query_db(query, user_data)
        return True
    
    @classmethod
    def update_user_profile(cls, user_data):  

        user_data = user_data.copy()
    
        this_user = cls.get_user_by_id(user_data['id'])

        if session['user_id'] != this_user.id:
            return False
        
        is_valid = cls.validate_user_profile(user_data)
        
        if not is_valid:
            return False
        
        query = """
                UPDATE users
                SET first_name = %(first_name)s,
                    last_name = %(last_name)s,
                    email = %(email)s
                WHERE id=%(id)s;    
                """
        connectToMySQL(cls.db).query_db(query, user_data)
        return True


    # Delete Users Models

    @classmethod
    def delete_user(cls, user_id):
        
        if session['user_id'] != user_id:
            return False
        
        data = {'id': user_id}

        query = """
                DELETE FROM users
                WHERE id = %(id)s;
        """
        
        return connectToMySQL(cls.db).query_db(query, data)

        if not result:
            return None

        return cls(result[0])
    
    # Validation

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
    
    @staticmethod
    def validate_user_profile(user):

        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

        is_valid = True
        if len(user['first_name']) < 4 or user['first_name'].isspace() or not user['first_name'].isalpha():
            flash("First name must be at least 3 letters long.", "error")
            is_valid = False
        if len(user['last_name']) < 4 or user['last_name'].isspace()or not user['last_name'].isalpha():
            flash("Last name must be at least 3 letters long.", "error")
            is_valid = False                 
        if len(user['email']) == 0  or user['email'].isspace():
            flash("Email is required.", "error")
            is_valid = False       
        elif not EMAIL_REGEX.match(user['email']):
            flash("Invalid email format.", "error")
            is_valid = False   
        if User.get_user_by_email(user['email']):
            if int(user['id']) != session['user_id']:  #okay for user to keep the same email, but don't want someone else using this email
                flash(f"{user['email']} is already taken.")
                return False
        return is_valid
    
    @staticmethod
    def validate_user_password(user):

        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

        is_valid = True
        
        if len(user['password']) < 8 or user['password'].isspace():
            flash("Password must be at least 8 characters long.", "error")
            is_valid = False
        elif user['password'] != user['confirm_password']:
            flash("Passwords do not match.", "error")
            is_valid = False
        if not User.string_contains_an_uppercase_letter(user['password']):
            flash("Password must contain at least one uppercase letter.", "error") 
            is_valid = False
        if not User.string_contains_a_number(user["password"]):
            flash("Password must contain at least one number.", "error") 
            is_valid = False                  
        return is_valid
    
    
    @staticmethod
    def validate_user_registration(user):

        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

        is_valid = True
        if len(user['first_name']) < 4 or user['first_name'].isspace() or not user['first_name'].isalpha():
            flash("First name must be at least 3 letters long.", "error")
            is_valid = False
        if len(user['last_name']) < 4 or user['last_name'].isspace()or not user['last_name'].isalpha():
            flash("Last name must be at least 3 letters long.", "error")
            is_valid = False
        if len(user['password']) < 8 or user['password'].isspace():
            flash("Password must be at least 8 characters long.", "error")
            is_valid = False
        elif user['password'] != user['confirm_password']:
            flash("Passwords do not match.", "error")
            is_valid = False
        if not User.string_contains_an_uppercase_letter(user['password']):
            flash("Password must contain at least one uppercase letter.", "error") 
            is_valid = False
        if not User.string_contains_a_number(user["password"]):
            flash("Password must contain at least one number.", "error") 
            is_valid = False                  
        if len(user['email']) == 0  or user['email'].isspace():
            flash("Email is required.", "error")
            is_valid = False       
        elif not EMAIL_REGEX.match(user['email']):
            flash("Invalid email format.", "error")
            is_valid = False
        if User.get_user_by_email(user['email']):
                flash(f"{user['email']} is already taken.")
                return False
        return is_valid 
    
    # determines if a string has at least one number in it
    @classmethod
    def string_contains_a_number(cls,str):
        for character in str:
            if character.isnumeric():
                return True
        return False 
    
    # determines if a string has at least one uppercase letter in it        
    @classmethod
    def string_contains_an_uppercase_letter(cls,str):
        for character in str:
            if character.isupper():
                return True 
        return False   
    
    # login and logout

    @classmethod
    def login_user(cls, data):
        email_to_check = data["email"]
        user_in_db = cls.get_user_by_email(email_to_check)

        if not user_in_db:
            flash(f"{email_to_check} is not registered.", "error")
            return False
        
        password_to_check = data["password"]
        if not bcrypt.check_password_hash(user_in_db.password, password_to_check):
            flash("Password does not match.", "error")
            return False
        
        session['user_id'] = user_in_db.id
        session['first_name'] = user_in_db.first_name
        session['logged_in'] = True

        return True
    
    
