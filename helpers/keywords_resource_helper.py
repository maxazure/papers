from flask_restful import fields, reqparse, inputs
from models.keyword import Keyword

paginate_fields = {
    'total': fields.Integer,
    'pageSize': fields.Integer,
    'current': fields.Integer
}

keyword_fields = {
    'id': fields.Integer,
    'name': fields.String,
    'related_papers': fields.String,

    'created_at': fields.String
}

keyword_list_fields = {
    'pagination': fields.Nested(paginate_fields),
    'list': fields.List(fields.Nested(keyword_fields))
}

sortable_fields = ['id',]

keyword_post_parser = reqparse.RequestParser()
keyword_post_parser.add_argument('name', type=str, )
keyword_post_parser.add_argument('related_papers', type=str, )


keyword_update_parser = reqparse.RequestParser()
keyword_update_parser.add_argument('name', type=str)
keyword_update_parser.add_argument('related_papers', type=str)



keyword_query_parser = reqparse.RequestParser()
keyword_query_parser.add_argument('name', type=str)
keyword_query_parser.add_argument('related_papers', type=str)


keyword_query_parser.add_argument('orderby', type=str, default='id')
keyword_query_parser.add_argument('desc', type=int, default=0)
keyword_query_parser.add_argument('page', type=int)
keyword_query_parser.add_argument('pagesize', type=int)

def make_conditions(conditions, args):
    if args['name'] is not None:
        conditions.append(Keyword.name.like('%'+args['name']+'%'))
    if args['related_papers'] is not None:
        conditions.append(Keyword.related_papers.like('%'+args['related_papers']+'%'))

    return conditions

def update_all_fields(args, o):
    if args['name']:
        o.name = args['name']
    if args['related_papers']:
        o.related_papers = args['related_papers']

    return o