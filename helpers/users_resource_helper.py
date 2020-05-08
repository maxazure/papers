from flask_restful import fields, reqparse, inputs
from models.user import User

paginate_fields = {
    'total': fields.Integer,
    'pageSize': fields.Integer,
    'current': fields.Integer
}

user_fields = {
    'id': fields.Integer,
    'name': fields.String,

    'email': fields.String,

    'first_language': fields.String,

    'intro': fields.String,

    'avatar': fields.String,


    'created_at': fields.String
}

user_list_fields = {
    'pagination': fields.Nested(paginate_fields),
    'list': fields.List(fields.Nested(user_fields))
}

sortable_fields = ['id',]

user_post_parser = reqparse.RequestParser()
user_post_parser.add_argument('name', type=str, )

user_post_parser.add_argument('email', type=str, )



user_post_parser.add_argument('first_language', type=str, )

user_post_parser.add_argument('intro', type=str, )

user_post_parser.add_argument('avatar', type=str, )



user_update_parser = reqparse.RequestParser()
user_update_parser.add_argument('name', type=str)

user_update_parser.add_argument('email', type=str)



user_update_parser.add_argument('first_language', type=str)

user_update_parser.add_argument('intro', type=str)

user_update_parser.add_argument('avatar', type=str)




user_query_parser = reqparse.RequestParser()
user_query_parser.add_argument('email', type=str)



user_query_parser.add_argument('orderby', type=str, default='id')
user_query_parser.add_argument('desc', type=int, default=0)
user_query_parser.add_argument('page', type=int)
user_query_parser.add_argument('pagesize', type=int)

def make_conditions(conditions, args):
    if args['email'] is not None:

        conditions.append(User.email==args['email'])


    return conditions

def update_all_fields(args, o):
    if args['name']:

        o.name = args['name']

    if args['first_language']:

        o.first_language = args['first_language']

    if args['intro']:

        o.intro = args['intro']

    if args['avatar']:

        o.avatar = args['avatar']


    return o