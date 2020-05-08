from flask_restful import fields, reqparse, inputs
from models.course import Course

paginate_fields = {
    'total': fields.Integer,
    'pageSize': fields.Integer,
    'current': fields.Integer
}

course_fields = {
    'id': fields.Integer,
    'name': fields.String,

    'created_at': fields.String
}

course_list_fields = {
    'pagination': fields.Nested(paginate_fields),
    'list': fields.List(fields.Nested(course_fields))
}

sortable_fields = ['id',]

course_post_parser = reqparse.RequestParser()
course_post_parser.add_argument('name', type=str, )


course_update_parser = reqparse.RequestParser()
course_update_parser.add_argument('name', type=str)



course_query_parser = reqparse.RequestParser()


course_query_parser.add_argument('orderby', type=str, default='id')
course_query_parser.add_argument('desc', type=int, default=0)
course_query_parser.add_argument('page', type=int)
course_query_parser.add_argument('pagesize', type=int)

def make_conditions(conditions, args):

    return conditions

def update_all_fields(args, o):
    if args['name']:
        o.name = args['name']

    return o