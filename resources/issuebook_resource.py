from models.books_model import issueBook
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
        bookissue = issueBook.borrow_status(**request_data)