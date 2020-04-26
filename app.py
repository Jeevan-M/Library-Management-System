from flask import Flask
from flask_restful import Api
from resources.users_resource import UserResource

app = Flask(__name__)
API=Api(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db' #'mysql://scott:tiger@localhost/mydatabase'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

@app.before_first_request
def create_tables():
    db_connect.create_all()            

API.add_resource(UserResource,'/register')

if __name__ == "__main__":
    from db_connection import db_connect
    db_connect.init_app(app)
    app.run(debug=True)