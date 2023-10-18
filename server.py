from flask_app import app
from flask_app.controllers import users, ideas


if __name__=="__main__":   
    app.run(debug=True, port=5001) 
    # i set my port to 5001 because the default port 5000 is used by airplay
    # On line six you can change the port number.

# debug needs to be set to False when deployed.
