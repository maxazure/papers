from sqlalchemy import ForeignKey, func
from app import db
from .base_model import BaseModel


class Course(BaseModel):
    __tablename__ = 'course'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))

    created_at = db.Column(db.DateTime, server_default=func.now())

    @staticmethod
    def find_by_id(id):
        return db.session.query(Course).filter(
            Course.id == id
        ).first()