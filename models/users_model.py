from db_connection import db_connect

class UserModel(db_connect.Model):
    __tablename__ = "users"
    id = db_connect.Column(db_connect.Integer,primary_key=True)
    name = db_connect.Column(db_connect.String(40))
    email = db_connect.Column(db_connect.String(40))
    usertype = db_connect.Column(db_connect.String(40))
    phone = db_connect.Column(db_connect.String(10))
    password = db_connect.Column(db_connect.String(100))
    nobookissue = db_connect.Column(db_connect.Integer)
    maxbook = db_connect.Column(db_connect.Integer)

    def __init__(self,Name,Email,Type,Phone,Password):
        self.name = Name
        self.email = Email
        self.usertype = Type
        self.phone = Phone
        self.password = Password
        self.nobookissue = 0
        self.maxbook = 10

    
    @classmethod
    def find_by_user_email(cls,email):
        return cls.query.filter_by(email=email).first()

    def save_to_db(self):
        db_connect.session.add(self)
        db_connect.session.commit()
    



