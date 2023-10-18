from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import user
from flask import flash

db = "brainstorm_visualizer"

class Idea:
    db = "brainstorm_visualizer"
    def __init__(self, data=None):
        if data is not None:
            self.id = data['id']
            self.main_idea = data['main_idea']
            self.cat_1 = data['cat_1']
            self.cat_2 = data['cat_2']
            self.cat_3 = data['cat_3']
            self.cat_4 = data['cat_4']
            self.cat_5 = data['cat_5']
            self.sub_c_1_1 = data['sub_c_1_1']
            self.sub_c_1_2 = data['sub_c_1_2']
            self.sub_c_1_3 = data['sub_c_1_3']
            self.sub_c_2_1 = data['sub_c_2_1']
            self.sub_c_2_2 = data['sub_c_2_2']
            self.sub_c_2_3 = data['sub_c_2_3']
            self.sub_c_3_1 = data['sub_c_3_1']
            self.sub_c_3_2 = data['sub_c_3_2']
            self.sub_c_3_3 = data['sub_c_3_3']
            self.sub_c_4_1 = data['sub_c_4_1']
            self.sub_c_4_2 = data['sub_c_4_2']
            self.sub_c_4_3 = data['sub_c_4_3']
            self.sub_c_5_1 = data['sub_c_5_1']
            self.sub_c_5_2 = data['sub_c_5_2']
            self.sub_c_5_3 = data['sub_c_5_3']
            self.users_id = data['users_id']
            self.first_name = data['first_name']
            self.last_name = data['last_name']


    @classmethod
    def read_all_ideas(cls):
        query = "SELECT * FROM ideas LEFT JOIN users ON users.id = ideas.users_id;"
        results = connectToMySQL(db).query_db(query)
        all_ideas = []

        for row in results:
            invention = cls(row) 
            all_ideas.append(invention)

        return all_ideas

    @classmethod
    def create_idea(cls,data):
        query = """
        INSERT INTO ideas(main_idea, cat_1, cat_2, cat_3, cat_4, cat_5,
        sub_c_1_1, sub_c_1_2, sub_c_1_3, sub_c_2_1, sub_c_2_2, sub_c_2_3, sub_c_3_1,
        sub_c_3_2, sub_c_3_3, sub_c_4_1, sub_c_4_2, sub_c_4_3, sub_c_5_1, sub_c_5_2, sub_c_5_3,
        users_id) 
        VALUES (%(main_idea)s, %(cat_1)s, %(cat_2)s, %(cat_3)s,%(cat_4)s,%(cat_5)s,
        %(sub_c_1_1)s,%(sub_c_1_2)s,%(sub_c_1_3)s,%(sub_c_2_1)s,%(sub_c_2_2)s,%(sub_c_2_3)s,%(sub_c_3_1)s,
        %(sub_c_3_2)s,%(sub_c_3_3)s,%(sub_c_4_1)s,%(sub_c_4_2)s,%(sub_c_4_3)s,%(sub_c_5_1)s,%(sub_c_5_2)s,%(sub_c_5_3)s,
        %(users_id)s);
        """
        connectToMySQL(db).query_db(query, data)


    @classmethod
    def get_idea_with_user(cls, data):
        query = "SELECT * FROM ideas LEFT JOIN users ON users.id = ideas.users_id WHERE ideas.id = %(id)s;"
        results = connectToMySQL(cls.db).query_db(query, data)
        if results:
            row = results[0]
            one_idea = cls(row)
            user_data = {
                "id": row['users.id'],
                "first_name": row['first_name'],
                "last_name": row['last_name'],
                "email": row['email'],
                "password": row['password'],
                "created_at": row['created_at'],
                "updated_at": row['updated_at'],
            }

            one_idea.user = user.User(user_data)

            return one_idea

    @classmethod
    def update(cls, data):
        query = """
        UPDATE ideas
        SET main_idea=%(main_idea)s, cat_1=%(cat_1)s, cat_2=%(cat_2)s,
        cat_3=%(cat_3)s, cat_iv=%(cat_4)s, cat_5=%(cat_5)s,
        sub_c_1_1=%(sub_c_1_1)s, sub_c_1_2=%(sub_c_1_2)s, sub_c_1_3=%(sub_c_1_3)s,
        sub_c_2_1=%(sub_c_2_1)s, sub_c_2_2=%(sub_c_2_2)s, sub_c_2_3=%(sub_c_2_3)s,
        sub_c_3_1=%(sub_c_3_1)s, sub_c_3_2=%(sub_c_3_2)s, sub_c_3_3=%(sub_c_3_3)s,
        sub_c_4_1=%(sub_c_4_1)s, sub_c_4_2=%(sub_c_4_2)s, sub_c_4_3=%(sub_c_4_3)s,
        sub_c_5_1=%(sub_c_5_1)s, sub_c_5_2=%(sub_c_5_2)s, sub_c_5_3=%(sub_c_5_3)s,
        WHERE id = %(id)s;
        """
        return connectToMySQL(cls.db).query_db(query, data)

    @classmethod
    def delete_idea(cls, data):
        query = "DELETE FROM ideas WHERE id = %(id)s;"
        connectToMySQL(cls.db).query_db(query, data)

    @staticmethod
    def valid(idea):
        is_valid = True
        if len(idea['main_idea']) < 3:
            flash("*Main idea must be at least 3 characters")
            is_valid = False
        # Add validation for other fields as needed
        return is_valid

