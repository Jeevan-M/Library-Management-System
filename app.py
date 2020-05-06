from flask import Flask
from flask_restful import Api
from flask_cors import CORS
from resources.users_resource import UserResource,UserResourceDetails,UserResourceLogin
from resources.books_resource import BooksResource
from resources.admin_resource import AdminLoginResource

app = Flask(__name__)
CORS(app)
endpoint_api = Api(app)
app.config['SQLALCHEMY_DATABASE_URI'] =  'mysql://root:''@localhost/lms' #'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

@app.before_first_request
def create_tables():
    db_connect.create_all()            


endpoint_api.add_resource(UserResourceDetails,'/user/<string:userid>')
endpoint_api.add_resource(UserResource,'/register')
endpoint_api.add_resource(UserResourceLogin,'/userlogin')
endpoint_api.add_resource(BooksResource,'/insertbook')
endpoint_api.add_resource(AdminLoginResource,'/AdminLogin')

if __name__ == "__main__":
    from db_connection import db_connect
    db_connect.init_app(app)
    app.run(debug=True)