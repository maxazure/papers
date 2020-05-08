from flask_restful import Resource, reqparse, request
from flask_restful import fields, marshal_with, marshal
from sqlalchemy.exc import IntegrityError
from sqlalchemy import or_, and_, text
from flask_jwt_extended import jwt_required
from models.paper import Paper
from app import db
from utils.util import max_res


from helpers.papers_resource_helper import *

class PapersResource(Resource):

    @jwt_required
    def get(self, paper_id=None):
        if paper_id:
            paper = Paper.find_by_id(paper_id)
            return max_res(marshal(paper, paper_fields))
        else:
            conditions = []

            args = paper_query_parser.parse_args()
            page = args['page']
            per_page = args['pagesize']

            if args['orderby'] not in sortable_fields:
                return max_res('', code=500, errmsg='排序非法字段')
            sort = args['orderby']
            if args['desc']>0:
                sort = args['orderby'] + ' desc'

            conditions = make_conditions(conditions,args)
            # 在这里添加更多的 条件查询 例如 
            # if args['name'] is not None:
            #       conditions.append(Paper.name.like('%'+args['name']+'%'))
       
            if conditions is []:
                pagination = Paper.query.order_by(text(sort)).paginate(page, per_page, error_out=False)
            else:
                pagination = Paper.query.filter(*conditions).order_by(text(sort)).paginate(page, per_page, error_out=False)
            paginate = {
                'total':pagination.total,
                'pageSize': pagination.per_page,
                'current': pagination.page
            }
            print(pagination.items)


            return max_res(marshal({
                'pagination': paginate,
                'list': [marshal(u, paper_fields) for u in pagination.items]
            }, paper_list_fields))


    @jwt_required
    def post(self):
        args = paper_post_parser.parse_args()

        paper = Paper(**args)
        try:
            paper.add()
        except IntegrityError:
            return max_res('', code=401, errmsg='名称重复')

        return max_res(marshal(paper, paper_fields))


   
    def put(self, paper_id=None):
        paper = Paper.find_by_id(paper_id)

        args = paper_update_parser.parse_args()

        paper = update_all_fields(args, paper)
        #可以在这里继续添加 需要更新的字段 如
        #    if args['name']:
        #       o.name = args['name']
        #
        
        db.session.commit()
        try:
            paper.update()
        except Exception as e:
            return max_res('',500, 'Failed to modify.')

        return max_res(marshal(paper, paper_fields))

   
    def delete(self, paper_id=None):
        paper = Paper.find_by_id(paper_id)

        try:
            paper.delete()
        except Exception as e:
            return max_res('',500, 'The record has already deleted.')

        return max_res('The paper has been deleted.')