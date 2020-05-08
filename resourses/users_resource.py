from flask_restful import Resource, reqparse, request
from flask_restful import fields, marshal_with, marshal
from sqlalchemy.exc import IntegrityError
from sqlalchemy import or_, and_, text
from flask_jwt_extended import jwt_required
from models.user import User
from app import db
from utils.util import max_res


from helpers.users_resource_helper import *


class UsersResource(Resource):

    @jwt_required
    def get(self, user_id=None):
        if user_id:
            user = User.find_by_id(user_id)
            return max_res(marshal(user, user_fields))
        else:
            conditions = []

            args = user_query_parser.parse_args()
            page = args['page']
            per_page = args['pagesize']

            if args['orderby'] not in sortable_fields:
                return max_res('', code=500, errmsg='排序非法字段')
            sort = args['orderby']
            if args['desc'] > 0:
                sort = args['orderby'] + ' desc'

            conditions = make_conditions(conditions, args)
            # 在这里添加更多的 条件查询 例如
            # if args['name'] is not None:
            #       conditions.append(User.name.like('%'+args['name']+'%'))

            if conditions is []:
                pagination = User.query.order_by(text(sort)).paginate(
                    page, per_page, error_out=False)
            else:
                pagination = User.query.filter(
                    *conditions).order_by(text(sort)).paginate(page, per_page, error_out=False)
            paginate = {
                'total': pagination.total,
                'pageSize': pagination.per_page,
                'current': pagination.page
            }
            print(pagination.items)

            return max_res(marshal({
                'pagination': paginate,
                'list': [marshal(u, user_fields) for u in pagination.items]
            }, user_list_fields))

    # TODO @jwt_required

    def post(self):
        user_post_parser.add_argument('password', type=str, )
        args = user_post_parser.parse_args()
        password = args['password']

        user = User(
            name=args['name'],
            email=args['email'],
            intro=args['intro'],
            avatar=args['avatar']
        )
        if(user.avatar == ''):
            user.avatar = 'https://avatars.dicebear.com/v2/female/janefaddsdfkk.svg'
        if(user.intro == ''):
            user.intro = 'Hi all.'

        user.set_password(password)
        try:
            user.add()
        except IntegrityError:
            return max_res('', code=500, errmsg='Record existed.')

        return max_res(marshal(user, user_fields))

    def put(self, user_id=None):
        user = User.find_by_id(user_id)
        user_update_parser.add_argument('password', type=str)
        args = user_update_parser.parse_args()

        user = update_all_fields(args, user)
        # 可以在这里继续添加 需要更新的字段 如
        #    if args['name']:
        #       o.name = args['name']
        #
        if args['password']:
            user.set_password(args['password'])

        db.session.commit()
        try:
            user.update()
        except Exception as e:
            return max_res('', 500, 'Failed to modify.')

        return max_res(marshal(user, user_fields))

    def delete(self, user_id=None):
        user = User.find_by_id(user_id)

        try:
            user.delete()
        except Exception as e:
            return max_res('', 500, 'The record has already deleted.')

        return max_res('The user has been deleted.')
