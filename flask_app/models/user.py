
from flask_app import app
from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash, session
# from flask_app.models import buyer  # may need to import other models
import re, datetime
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)


class User:
    db = "name_of_database_here" 
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.password = data['password']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        
    # Create Users Models

    # class method to save our user to the database
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

    # @classmethod   can be modified to accommodate get_one_user_by_id_with_all_mindmaps 
    # def get_one_user_by_id_with_all_buyers(cls, user_id):

    #     data = {'id' : user_id}

    #     query = """
    #             SELECT * FROM users
    #             LEFT JOIN buyers
    #             ON users.id = buyers.user_id
    #             WHERE users.id = %(id)s;
    #             """
    #     results = connectToMySQL(cls.db).query_db(query, data)
    #     this_user = cls(results[0])
    #     if results[0]['buyers.id']:
    #         for result in results:
    #             this_user.all_buyers.append(buyer.Buyer({
    #                 'id' : result['buyers.id'],
    #                 'first_name' : result['buyers.first_name'],
    #                 'last_name' : result['buyers.last_name'],
    #                 'status' : result['status'],
    #                 'created_at' : result['buyers.created_at'],
    #                 'updated_at' : result['buyers.updated_at'],
    #                 'user_id' : result['user_id'],
    #             }))
    #     return this_user


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


    # Update Users Models

    
    # Validation
    
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
        






