from sqlalchemy import ForeignKey, func
from app import bcrypt, db
from .base_model import BaseModel


class User(BaseModel):
    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String())

    email = db.Column(db.String(), nullable=False, unique=True)

    password_hash = db.Column(db.String(), nullable=False)

    intro = db.Column(db.String())

    avatar = db.Column(db.String())


    created_at = db.Column(db.DateTime, server_default=func.now())

    def set_password(self, password):
        self.password_hash = bcrypt.generate_password_hash(password)

    def check_password(self, password):
        return bcrypt.check_password_hash(self.password_hash, password)

   

    @staticmethod
    def find_by_id(id):
        return db.session.query(User).filter(
            User.id == id
        ).first()

    @staticmethod
    def find_by_email(email):
        return db.session.query(User).filter(
            User.email == email
        ).first()