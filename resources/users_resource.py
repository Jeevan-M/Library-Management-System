from flask_restful import Resource,reqparse
from models.users_model import UserModel

class UserResource(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument(
        'Name',
        type=str,
        required=True,
        help='Name field is required'
    )
    parser.add_argument(
        'Email',
        type=str,
        required=True,
        help='Email field is required'
    )
    parser.add_argument(
        'Type',
        type=str,
        required=True,
        help='Type field is required'
    )
    parser.add_argument(
        'Phone',
        type=int,
        required=True,
        help='Phone field is required'
    )
    parser.add_argument(
        'Password',
        type=int,
        required=True,
        help='Password field is required'
    )
    def post(self):
        request_data = UserResource.parser.parse_args()
        if UserModel.find_by_user_email(request_data['Email']):
            return {'Message': 'The email is already exist'},400
        user_register = UserModel(**request_data)
        try:
            user_register.save_to_db()
        except:
            return {'Message':'An Internal Server Error occurred While Register the user'},500
        return {'Message':'Registerd Successfully.....!'}

    



