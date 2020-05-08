from sqlalchemy import ForeignKey, func
from app import db
from .base_model import BaseModel


class Keyword(BaseModel):
    __tablename__ = 'keyword'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    related_papers = db.Column(db.Text)

    created_at = db.Column(db.DateTime, server_default=func.now())

    @staticmethod
    def find_by_id(id):
        return db.session.query(Keyword).filter(
            Keyword.id == id
        ).first()