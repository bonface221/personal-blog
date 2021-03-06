from . import db
from flask_login import UserMixin
from . import login_manager
from werkzeug.security import generate_password_hash,check_password_hash

class Quote:
    def __init__(self,author,quote):
        self.author=author
        self.quote=quote


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class User(UserMixin, db.Model):
    __tablename__='users'
    id = db.Column(db.Integer,primary_key=True)
    username = db.Column(db.String(255),index = True)
    email= db.Column(db.String(255),unique = True, index = True)
    pass_secure = db.Column(db.String(455))
    blogs=db.relationship('Blogs',backref='user',lazy='dynamic')
    
    @property
    def password(self):
        raise AttributeError('password is not a readable attribute')

    @property
    def password(self):
        raise AttributeError('You cannot read the password attribute')

    @password.setter
    def password(self,password):
        self.pass_secure = generate_password_hash(password, method='pbkdf2:sha256', salt_length=8)

    def verify_password(self,password):
        return check_password_hash(self.pass_secure,password)

    
    def __repr__(self):
        return f'User {self.username}'

class Blogs(db.Model):
    __tablename__='blogs'
    id = db.Column(db.Integer, primary_key=True)
    title=db.Column(db.String(255))
    description=db.Column(db.String(255))
    user_id = db.Column(db.Integer,db.ForeignKey('users.id'))
    
 
    def __repr__(self):
        return self.title
