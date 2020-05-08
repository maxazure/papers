from flask import Flask, jsonify, request, json
from flask.helpers import flash, url_for
from werkzeug.utils import redirect, secure_filename
import os, time, codecs
from datetime import datetime
from app import app
from utils.util import max_res
from werkzeug.routing import BaseConverter

class RegexConverter(BaseConverter):
    def __init__(self, url_map,*items):
        super(RegexConverter,self).__init__(url_map)
        self.regex = items[0]



app.url_map.converters['reg'] = RegexConverter

@app.route('/')
def index():
    return app.send_static_file('index.html')

@app.route('/hi/<reg(".*?"):url>')
def hi(url):
    return  'hi, world. url:' + url + str(request.args.get('b'))