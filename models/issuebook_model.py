from db_connection import db_connect
import datetime 

class issueBook(db_connect.Model):
    __tablename__ = 'issuebook'
    id = db_connect.Column(db_connect.Integer,primary_key=True)
    bookid = db_connect.Column(db_connect.Integer,db_connect.ForeignKey('allbooks.bookid'))
    book = db_connect.relationship('BookModel')
    userid = db_connect.Column(db_connect.Integer,db_connect.ForeignKey('users.userid'))
    user = db_connect.relationship('UserModel')
    status = db_connect.Column(db_connect.String(10))
    borrow_date = db_connect.Column(db_connect.Date)
    return_date = db_connect.Column(db_connect.Date)

    def __init__(self,LMSBOOKID,LMSID):
        self.bookid = LMSBOOKID
        self.userid = LMSID
        self.status = 'Bookissued'
        self.borrow_date = datetime.date.today()
        self.return_date = datetime.date.today() + datetime.timedelta(days=10)


    @classmethod
    def borrow_status(cls,LMSBOOKID,LMSID):
        return cls.query.filter_by(ans_(bookid=LMSBOOKID ,userid=LMSID))

    def issue_the_book(self):
        db_connect.session.add(self)
        db_connect.session.commit()