from flask_app import app
from flask_app.controllers import users, ideas


if __name__=="__main__":   
    app.run(debug=True) 
    # On line six you can change the port number.

# debug needs to be set to False when deployed.
