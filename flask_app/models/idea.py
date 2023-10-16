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
            self.cat_i = data['cat_i']
            self.cat_ii = data['cat_ii']
            self.cat_iii = data['cat_iii']
            self.cat_iv = data['cat_iv']
            self.cat_v = data['cat_v']
            self.sub_c_i = data['sub_c_i']
            self.sub_c_ii = data['sub_c_ii']
            self.sub_c_iii = data['sub_c_iii']
            self.sub_c_iv = data['sub_c_iv']
            self.sub_c_v = data['sub_c_v']
            self.sub_c_vi = data['sub_c_vi']
            self.sub_c_vii = data['sub_c_vii']
            self.sub_c_viii = data['sub_c_viii']
            self.sub_c_ix = data['sub_c_ix']
            self.sub_c_x = data['sub_c_x']
            self.sub_c_xi = data['sub_c_xi']
            self.sub_c_xii = data['sub_c_xii']
            self.sub_c_xiii = data['sub_c_xiii']
            self.sub_c_xiv = data['sub_c_xiv']
            self.sub_c_xv = data['sub_c_xv']
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
        INSERT INTO ideas(main_idea, cat_i, cat_ii, cat_iii, cat_iv, cat_v,
        sub_c_i, sub_c_ii, sub_c_iii, sub_c_iv, sub_c_v, sub_c_vi, sub_c_vii,
        sub_c_viii, sub_c_ix, sub_c_x, sub_c_xi, sub_c_xii, sub_c_xiii, sub_c_xiv, sub_c_xv,
        users_id) 
        VALUES (%(main_idea)s, %(cat_i)s, %(cat_ii)s, %(cat_iii)s,%(cat_iv)s,%(cat_v)s,
        %(sub_c_i)s,%(sub_c_ii)s,%(sub_c_iii)s,%(sub_c_iv)s,%(sub_c_v)s,%(sub_c_vi)s,%(sub_c_vii)s,
        %(sub_c_viii)s,%(sub_c_ix)s,%(sub_c_x)s,%(sub_c_xi)s,%(sub_c_xii)s,%(sub_c_xiii)s,%(sub_c_xiv)s,%(sub_c_xv)s,
        %(users_id)s);
        """
        results = connectToMySQL(db).query_db(query, data)


    @classmethod
    def get_one_with_user(cls, data):
        query = "SELECT * FROM ideas LEFT JOIN users ON users.id = ideas.users_id WHERE ideas.id = %(id)s;"
        results = connectToMySQL(cls.db).query_db(query, data)
        if results:
            row = results[0]
            one_idea = cls(row)
            user_data = {
                "id": row['users.id'],
                "first_name": row['first_name'],
                "last_name": row['last_name'],
                # Add other user attributes as needed
                #"email": row['email'],
                #"password": row['password'],
                #"created_at": row['users.created_at'],
                #"updated_at": row['users.updated_at'],
            }

            one_idea.user = user.User(user_data)

            return one_idea

    @classmethod
    def update(cls, data):
        query = """
        UPDATE ideas
        SET main_idea=%(main_idea)s, cat_i=%(cat_i)s, cat_ii=%(cat_ii)s,
        cat_iii=%(cat_iii)s, cat_iv=%(cat_iv)s, cat_v=%(cat_v)s,
        sub_c_i=%(sub_c_i)s, sub_c_ii=%(sub_c_ii)s, sub_c_iii=%(sub_c_iii)s,
        sub_c_iv=%(sub_c_iv)s, sub_c_v=%(sub_c_v)s, sub_c_vi=%(sub_c_vi)s,
        sub_c_vii=%(sub_c_vii)s, sub_c_viii=%(sub_c_viii)s, sub_c_ix=%(sub_c_ix)s,
        sub_c_x=%(sub_c_x)s, sub_c_xi=%(sub_c_xi)s, sub_c_xii=%(sub_c_xii)s,
        sub_c_xiii=%(sub_c_xiii)s, sub_c_xiv=%(sub_c_xiv)s, sub_c_xv=%(sub_c_xv)s
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

