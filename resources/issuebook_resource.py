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
        
        #find the count of borrowed book by the user
        user_borrow_count = issueBook.find_user_count(request_data['LMSID'])
        if user_borrow_count >= 10:
            return {'Message' : 'You reached maximum limite to borrow this book','status':400},400
        
        #checking the book avaliablity 
        book_avaliable_check = BookModel.find_by_bookid(request_data['LMSBOOKID'])
        if book_avaliable_check.remainingbook == 0:
            return {'Message' : 'Sorry Book not Avaliable','status':400},400
        
        #check the user already borrow this book
        if issueBook.borrow_status(**request_data):
            return {'Message':'This Book You Already Borrowed','status':400},400
        
        #user detail to update the number of books borrowed
        usercheck = UserModel.find_by_user_userid(request_data['LMSID'])
        borrowed_book_count = issueBook.find_book_count(request_data['LMSBOOKID'])
        if borrowed_book_count == 0:
            borrowed_book_count = book_avaliable_check.remainingbook
        bookissue = issueBook(**request_data)
        try:
            if bookissue.issueTheBook():
                usercheck.nobookissue = user_borrow_count + 1
                book_avaliable_check.remainingbook = borrowed_book_count - 1
                usercheck.saveUserToDB()
                book_avaliable_check.saveBookToDB()
                return {'Message':'Book as been borrow Successfully','status':201},201
        except:
            return {'Message':'Internal Server Error While borrow the book','status':500},500
        

    def delete(self):
        request_data = issueBookResource.parser.parse_args()
        returnbook = issueBook.borrow_status(**request_data)
        if returnbook:
            usercheck = UserModel.find_by_user_userid(request_data['LMSID'])
            book_avaliable_check = BookModel.find_by_bookid(request_data['LMSBOOKID'])
            if returnbook.returnBookDelete():
                usercheck.nobookissue -= 1
                book_avaliable_check.remainingbook += 1 
                usercheck.saveUserToDB()
                book_avaliable_check.saveBookToDB()
            return {'Message':'Book Returned Successfully','status':200}
        return {'Message':'Uable to return Book'} 
