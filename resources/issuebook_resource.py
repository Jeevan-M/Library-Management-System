from models.issuebook_model import issueBook
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
        if issueBook.borrow_status(**request_data):
            return {'Message':'This Book You Already Borrowed','status':400},400
        bookissue = issueBook(**request_data)
        try:
            bookissue.issue_the_book()
            return {'Message':'Book as been borrow Successfully','status':201},201
        except:
            return {'Message':'Internal Server Error While borrow the book','status':500},500
        
    
