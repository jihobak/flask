from datetime import datetime
from app import db, login
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin


class User(UserMixin, db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True)
    password_hash = db.Column(db.String(128))
    # For a one-to-many relationship, a db.relationship field is normally defined on the "one"sie,
    # and is used as aconvenient way to get access to the "many"
    # The 'backref' argument defines the name of a filed that will be added to the objects of the
    # 'many' class that oints back at the "one" object.
    posts = db.relationship('Post', backref='author', lazy='dynamic')

    def __repr__(self):
        return "<User {}>".format(self.username)
    
    def set_password(self, password):
        self.password_hash = generate_password_hash(password)
    
    def check_password(self, password):
        return check_password_hash(self.password_hash, password)


# Each time the logged-in user navigated to a new page, Flask-Login retrieves the ID of
# of the user from the session, and then loads that user into memory.
@login.user_loader
def load_user(id):
    return User.query.get(int(id))

class Post(db.Model):
    __tablename__ = 'posts'
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.String(140))
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id')) #user is name of the database table

    def __repr__(self):
        return "<Post {}>".format(self.body)