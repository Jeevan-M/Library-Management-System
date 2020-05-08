from models.issuebook_model import issueBook
from models.users_model import UserModel
from models.books_model import BookModel
from flask_restful import Resource,reqparse

class issueBookResource(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument(
        'LMSBOOKID',
        type=str,
        required=True
    ),
    parser.add_argument(
        'LMSID',
        type=str,
        required=True
    )

    def post(self):
        request_data = issueBookResource.parser.parse_args()
        
        user_borrow_count = issueBook.find_user_count(request_data['LMSID'])
        if user_borrow_count >= 10:
            return {'Message' : 'You reached maximum limite to borrow this book','status':400},400
        
        
        
        if issueBook.borrow_status(**request_data):
            return {'Message':'This Book You Already Borrowed','status':400},400

        usercheck = UserModel.find_by_user_userid(request_data['LMSID'])
        
        bookissue = issueBook(**request_data)
        try:
            if bookissue.issue_the_book():
                usercheck.nobookissue = user_borrow_count + 1
                usercheck.save_to_db() 
                return {'Message':'Book as been borrow Successfully','status':201,'c':usercheck.nobookissue},201
        except:
            return {'Message':'Internal Server Error While borrow the book','status':500},500
        
    
