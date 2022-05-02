from .. import db, flask_bcrypt
import datetime
import jwt

from ..config import key

class Supervisor(db.Model):
    """ Supervisor Model for storing supervisor related details."""
    __tablename__ = "supervisor"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    email = db.Column(db.String, unique=True, nullable=False)
    name = db.Column(db.String, nullable=False)
    password_hash = db.Column(db.String)
    active = db.Column(db.Boolean, default=False)
    phone = db.Column(db.String, unique=True, nullable=False)
    role = db.Column(db.String, default='supervisor')
    email_verified_at = db.Column(db.DateTime, nullable=True)
    phone_verified_at = db.Column(db.DateTime, nullable=True)
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())
    updated_at = db.Column(db.DateTime,
                           default=db.func.current_timestamp(),
                           onupdate=db.func.current_timestamp())
    deleted_at = db.Column(db.DateTime, nullable=True)


    @property
    def password(self):
        raise AttributeError("password write only field")

    @password.setter
    def password(self, password):
        self.password_hash = flask_bcrypt.generate_password_hash(password).decode('utf-8')

    def check_password(self, password):
        return flask_bcrypt.check_password_hash(self.password_hash,password)

    def __repr__(self):
        return "Supervisor '{}'".format(self.email)