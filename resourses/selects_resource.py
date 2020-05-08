from flask_restful import Resource, reqparse, request
from flask_restful import fields, marshal_with, marshal
from sqlalchemy.exc import IntegrityError
from sqlalchemy import or_, and_, text
from flask_jwt_extended import jwt_required
from models.course import Course
from app import db
from utils.util import max_res
import json


class SelectsResource(Resource):
    @jwt_required
    def get(self, course_id=None):
        res = Course.query.all()
        res_list = []

        if (res != None):
            for item in res:
                res_list.append({'id': item.id, 'name': item.name})

        return max_res(res_list)
