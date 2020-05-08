from sqlalchemy import ForeignKey, func
from app import db
from .base_model import BaseModel


class Paper(BaseModel):
    __tablename__ = 'paper'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255))
    abstract = db.Column(db.Text)
    authors = db.Column(db.String(255))
    keywords = db.Column(db.String(255))
    url = db.Column(db.String(255))
    Published_year = db.Column(db.Integer)
    pdf = db.Column(db.String(255))
    title_cn = db.Column(db.String(255))
    abstract_cn = db.Column(db.Text)
    introduction = db.Column(db.Text)
    introduction_cn = db.Column(db.Text)
    conclusion = db.Column(db.Text)
    conclusion_cn = db.Column(db.Text)
    course = db.Column(db.String(80))
    catalog_id = db.Column(db.Integer)

    created_at = db.Column(db.DateTime, server_default=func.now())

    @staticmethod
    def find_by_id(id):
        return db.session.query(Paper).filter(
            Paper.id == id
        ).first()