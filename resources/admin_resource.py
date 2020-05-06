from flask_restful import Resource,reqparse
from models.admin_model import AdminModel
from werkzeug.security import check_password_hash

class AdminLoginResource(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument(
        'username',
        type=str,
        required=True,
        help='This username  Field is required'
    )
    parser.add_argument(
        'password',
        type=str,
        required=True,
        help='This password Field is required'
    )
    def post(self):
        request_data = AdminLoginResource.parser.parse_args()
        admin = AdminModel.find_by_username(request_data['username'])
        try:    
            if admin and check_password_hash(admin.password,request_data['password']):
                return {'Message':'Admin Login Successfull','status':200}
        except:
            return {'Message':'Internal Server Error','status':500},500
        return {'Message':'Admin Login Falied....','status':400},400

