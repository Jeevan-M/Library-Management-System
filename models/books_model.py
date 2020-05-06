from db_connection import db_connect
import datetime 
import random

class BookModel(db_connect.Model):
    __tablename__ = "allbooks"
    id = db_connect.Column(db_connect.Integer,primary_key=True)
    bookid = db_connect.Column(db_connect.String(20),unique=True)
    authorname = db_connect.Column(db_connect.String(40))
    bookname = db_connect.Column(db_connect.String(40))
    totalbook = db_connect.Column(db_connect.Integer)
    remainingbook = db_connect.Column(db_connect.Integer)

    book = db_connect.relationship('issueBook',lazy='dynamic')

    def __init__(self,AuthorName,BookName,TotalBook):
        self.bookid = 'LMSBOOKID'+str(random.randrange(1111,9999))
        self.authorname = AuthorName
        self.bookname = BookName
        self.totalbook = TotalBook
        self.remainingbook = 0
    
    def save_to_db(self):
        db_connect.session.add(self)
        db_connect.session.commit()

    @classmethod
    def find_by_bookname(cls,bookname):
        return cls.query.filter_by(bookname=bookname).first()

    def delete(self):
        db_connect.session.delete(self)
        db_connect.session.commit()

class issueBook(db_connect.Model):
    __tablename__ = 'issuebooke'
    id = db_connect.Column(db_connect.Integer,primary_key=True)
    bookid = db_connect.Column(db_connect.Integer,db_connect.ForeignKey('bookid'))
    userid = db_connect.Column(db_connect.Integer,db_connect.ForeignKey('userid'))
    status = db_connect.Column(db_connect.String(10))
    borrow_date = db_connect.Column(db_connect.DateTime)
    return_date = db_connect.Column(db_connect.DateTime)
    book = db_connect.relationship('BookModel')
    user = db_connect.relationship('UserModel')

    def __init__(self,LMSBOOKID,LMSID):
        self.bookid = LMSBOOKID
        self.userid = LMSID
        self.status = 'Bookissued'
        self.borrow_date = datetime.date.today()
        self.return_date = datetime.date.today() + datetime.timedelta(days=10)


    @classmethod
    def borrow_status(cls,bookid,userid):
        return cls.query.filter_by(bookid=bookid and userid=userid)

    def issue_the_book(self):
        db_connect.session.add(self)
        db_connect.session.commit()

    