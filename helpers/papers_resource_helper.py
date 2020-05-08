from flask_restful import fields, reqparse, inputs
from models.paper import Paper

paginate_fields = {
    'total': fields.Integer,
    'pageSize': fields.Integer,
    'current': fields.Integer
}

paper_fields = {
    'id': fields.Integer,
    'title': fields.String,
    'abstract': fields.String,
    'authors': fields.String,
    'keywords': fields.String,
    'url': fields.String,
    'Published_year': fields.Integer,
    'pdf': fields.String,
    'title_cn': fields.String,
    'abstract_cn': fields.String,
    'introduction': fields.String,
    'introduction_cn': fields.String,
    'conclusion': fields.String,
    'conclusion_cn': fields.String,
    'course': fields.String,
    'catalog_id': fields.Integer,

    'created_at': fields.String
}

paper_list_fields = {
    'pagination': fields.Nested(paginate_fields),
    'list': fields.List(fields.Nested(paper_fields))
}

sortable_fields = ['id',]

paper_post_parser = reqparse.RequestParser()
paper_post_parser.add_argument('title', type=str, )
paper_post_parser.add_argument('abstract', type=str, )
paper_post_parser.add_argument('authors', type=str, )
paper_post_parser.add_argument('keywords', type=str, )
paper_post_parser.add_argument('url', type=str, )
paper_post_parser.add_argument('Published_year', type=int, )
paper_post_parser.add_argument('pdf', type=str, )
paper_post_parser.add_argument('title_cn', type=str, )
paper_post_parser.add_argument('abstract_cn', type=str, )
paper_post_parser.add_argument('introduction', type=str, )
paper_post_parser.add_argument('introduction_cn', type=str, )
paper_post_parser.add_argument('conclusion', type=str, )
paper_post_parser.add_argument('conclusion_cn', type=str, )
paper_post_parser.add_argument('course', type=str, )
paper_post_parser.add_argument('catalog_id', type=int, )


paper_update_parser = reqparse.RequestParser()
paper_update_parser.add_argument('title', type=str)
paper_update_parser.add_argument('abstract', type=str)
paper_update_parser.add_argument('authors', type=str)
paper_update_parser.add_argument('keywords', type=str)
paper_update_parser.add_argument('url', type=str)
paper_update_parser.add_argument('Published_year', type=int)
paper_update_parser.add_argument('pdf', type=str)
paper_update_parser.add_argument('title_cn', type=str)
paper_update_parser.add_argument('abstract_cn', type=str)
paper_update_parser.add_argument('introduction', type=str)
paper_update_parser.add_argument('introduction_cn', type=str)
paper_update_parser.add_argument('conclusion', type=str)
paper_update_parser.add_argument('conclusion_cn', type=str)
paper_update_parser.add_argument('course', type=str)
paper_update_parser.add_argument('catalog_id', type=int)



paper_query_parser = reqparse.RequestParser()
paper_query_parser.add_argument('title', type=str)
paper_query_parser.add_argument('abstract', type=str)
paper_query_parser.add_argument('authors', type=str)
paper_query_parser.add_argument('keywords', type=str)
paper_query_parser.add_argument('url', type=str)
paper_query_parser.add_argument('Published_year', type=int)
paper_query_parser.add_argument('title_cn', type=str)
paper_query_parser.add_argument('abstract_cn', type=str)
paper_query_parser.add_argument('introduction', type=str)
paper_query_parser.add_argument('introduction_cn', type=str)
paper_query_parser.add_argument('conclusion', type=str)
paper_query_parser.add_argument('conclusion_cn', type=str)
paper_query_parser.add_argument('course', type=str)
paper_query_parser.add_argument('catalog_id', type=int)


paper_query_parser.add_argument('orderby', type=str, default='id')
paper_query_parser.add_argument('desc', type=int, default=0)
paper_query_parser.add_argument('page', type=int)
paper_query_parser.add_argument('pagesize', type=int)

def make_conditions(conditions, args):
    if args['title'] is not None:
        conditions.append(Paper.title.like('%'+args['title']+'%'))
    if args['abstract'] is not None:
        conditions.append(Paper.abstract.like('%'+args['abstract']+'%'))
    if args['authors'] is not None:
        conditions.append(Paper.authors.like('%'+args['authors']+'%'))
    if args['keywords'] is not None:
        conditions.append(Paper.keywords.like('%'+args['keywords']+'%'))
    if args['url'] is not None:
        conditions.append(Paper.url.like('%'+args['url']+'%'))
    if args['Published_year'] is not None:
        conditions.append(Paper.Published_year>args['Published_year'])
    if args['title_cn'] is not None:
        conditions.append(Paper.title_cn==args['title_cn'])
    if args['abstract_cn'] is not None:
        conditions.append(Paper.abstract_cn==args['abstract_cn'])
    if args['introduction'] is not None:
        conditions.append(Paper.introduction.like('%'+args['introduction']+'%'))
    if args['introduction_cn'] is not None:
        conditions.append(Paper.introduction_cn.like('%'+args['introduction_cn']+'%'))
    if args['conclusion'] is not None:
        conditions.append(Paper.conclusion.like('%'+args['conclusion']+'%'))
    if args['conclusion_cn'] is not None:
        conditions.append(Paper.conclusion_cn.like('%'+args['conclusion_cn']+'%'))
    if args['course'] is not None:
        conditions.append(Paper.course.like('%'+args['course']+'%'))
    if args['catalog_id'] is not None:
        conditions.append(Paper.catalog_id==args['catalog_id'])

    return conditions

def update_all_fields(args, o):
    if args['title']:
        o.title = args['title']
    if args['abstract']:
        o.abstract = args['abstract']
    if args['authors']:
        o.authors = args['authors']
    if args['keywords']:
        o.keywords = args['keywords']
    if args['url']:
        o.url = args['url']
    if args['Published_year']:
        o.Published_year = args['Published_year']
    if args['pdf']:
        o.pdf = args['pdf']
    if args['title_cn']:
        o.title_cn = args['title_cn']
    if args['abstract_cn']:
        o.abstract_cn = args['abstract_cn']
    if args['introduction']:
        o.introduction = args['introduction']
    if args['introduction_cn']:
        o.introduction_cn = args['introduction_cn']
    if args['conclusion']:
        o.conclusion = args['conclusion']
    if args['conclusion_cn']:
        o.conclusion_cn = args['conclusion_cn']
    if args['course']:
        o.course = args['course']
    if args['catalog_id']:
        o.catalog_id = args['catalog_id']

    return o