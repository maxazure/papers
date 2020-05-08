from flask import Flask, jsonify, request, json
from flask.helpers import flash, send_from_directory, url_for
from werkzeug.utils import redirect, secure_filename
import os, time, codecs
from datetime import datetime
from app import app
from utils.util import max_res

ALLOWED_EXTENSIONS = {'doc', 'pdf', 'docx'}

def mkdir(path):
    path=path.strip()
    path=path.rstrip("\\")
    isExists=os.path.exists(path)
    if not isExists:
        # 如果不存在则创建目录,创建目录操作函数
        os.makedirs(path) 
        print(path+' 创建成功')
        return True
    else:
        # 如果目录存在则不创建，并提示目录已存在
        print(path+' 目录已存在')
        return False

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/uploads/<path:path>')
def send_js(path):
 return send_from_directory('uploads', path)


@app.route('/api/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            return max_res('',404, 'No file part')
        file = request.files['file']
        # if user does not select file, browser also
        # submit an empty part without filename
        if file.filename == '':
            return max_res('',404, 'No selected file')
        if file and allowed_file(file.filename):
            today = datetime.utcnow().strftime("%Y%m%d")
            new_filename = datetime.utcnow().strftime("%H%M%S%f") + '.' + file.filename.rsplit('.', 1)[1].lower()
            upload_dir = app.config['UPLOAD_FOLDER']+ '/' + today
            mkdir(upload_dir)
            filename = secure_filename(file.filename)
            file.save(os.path.join(upload_dir, new_filename))
            return max_res('/uploads/'+ today + '/' +new_filename)
    return '''
    <!doctype html>
    <title>Upload new File</title>
    <h1>Upload new File</h1>
    <form method=post enctype=multipart/form-data>
      <input type=file name=file>
      <input type=submit value=Upload>
    </form>
    '''