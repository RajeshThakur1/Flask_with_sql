from .. import db, flask_bcrypt
import datetime
import jwt

from ..config import key

class SuperAdmin(db.Model):
    """superadmin table contains superadmin related information"""
    __tablename__ ="super_admin"

    id = db.Column(db.Integer, primary_key=True,autoincrement=True)
    email = db.Column(db.String, unique=True, nullable=False)
    name = db.Column(db.String, nullable=False)
    password_hash = db.Column(db.String)
    active = db.Column(db.Boolean, default=True)
    phone = db.Column(db.String, unique=True, nullable=False)
    role = db.Column(db.String, role = "super_admin")
    email_verified_at =db.Column(db.DateTime, nullable= True)
    phone_verified_at = db.Column(db.DateTime, nullable=True)
    created_at = db.Column(db.DateTime, default= db.func.current_timestamp())
    updated_at = db.Column(db.DateTime, default= db.func.current_timestamp(), onupdate= db.func.current_timestamp())
    deleted_at = db.Column(db.DateTime, nullable=True)