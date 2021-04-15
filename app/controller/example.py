from flask_restplus import Resource, Api, reqparse, fields, Namespace
from app import utils
from . import base_query_fields, ARLResource, get_arl_parser


ns = Namespace('example', description="这是一个example")


@ns.route('/')
class ContollerExample(ARLResource):

    def get(self):

        return "ok"