from db_connection import db_connect
from werkzeug.security import generate_password_hash
import random

class UserModel(db_connect.Model):
    __tablename__ = "users"
    id = db_connect.Column(db_connect.Integer,primary_key=True)
    name = db_connect.Column(db_connect.String(40))
    email = db_connect.Column(db_connect.String(40),unique=True)
    usertype = db_connect.Column(db_connect.String(40))
    phone = db_connect.Column(db_connect.String(10))
    password = db_connect.Column(db_connect.String(100))
    userid = db_connect.Column(db_connect.String(50),unique=True)
    nobookissue = db_connect.Column(db_connect.Integer)
    maxbook = db_connect.Column(db_connect.Integer)

    def __init__(self,Name,Email,Type,Phone,Password):
        self.name = Name
        self.email = Email
        self.usertype = Type
        self.phone = Phone
        self.password = generate_password_hash(Password)
        self.userid = 'LMSID'+str(random.randrange(1111, 9999))
        self.nobookissue = 0
        self.maxbook = 10

    def json(self):
        return {
    "Userid":self.userid,
	"Name":self.name,
	"Email":self.email,	
	"Type":self.usertype,
	"Phone":self.phone,
	"nobookissue":self.nobookissue,
    "maxbook":self.maxbook
}
    
    @classmethod
    def find_by_user_email(cls,email):
        return cls.query.filter_by(email=email).first()

    @classmethod
    def find_by_user_userid(cls,userid):
        return cls.query.filter_by(userid=userid).first()

    def save_to_db(self):
        db_connect.session.add(self)
        db_connect.session.commit()
    



