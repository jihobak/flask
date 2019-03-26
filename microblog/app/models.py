from datetime import datetime
from app import db


class User(db.Model):
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


class Post(db.Model):
    __tablename__ = 'posts'
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.String(140))
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id')) #user is name of the database table

    def __repr__(self):
        return "<Post {}>".format(self.body)