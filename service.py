import os
from flask import Flask, jsonify, request, send_from_directory, render_template
from flask_cors import CORS
from models.Items import Items
from base import Session, Base, engine
from werkzeug.utils import secure_filename
from pathlib import Path
import time
import json


app = Flask(__name__, static_url_path='')
CORS(app)

# generate database schema
Base.metadata.create_all(engine)

# create a new session
session = Session()

UPLOAD_FOLDER = str(Path.cwd()) + "/uploads"
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])

app.config['SQLALCHEMY_POOL_RECYCLE'] = 3600

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route("/")
def hello():
    return render_template("index.html")


@app.route('/uploads/<path:path>')
def send_js(path):
    return send_from_directory('uploads', path)


@app.route("/items", methods=['GET'])
def get_items():
    # Query the items
    # our_users = session.query(Items).filter_by(name='jesper').all()
    items = session.query(Items).all()
    results = []
    for item in items:
        results.append(item.as_dict())

    return jsonify(results)


@app.route("/insert", methods=['POST'])
def insert():
    item_args = {}
    # print(request.form['data'])
    if 'data' not in request.form:
        resp = jsonify({'message': 'No data part in the request'})
        resp.status_code = 400
        return resp

    # check if the post request has the file part
    # if 'file' not in request.files:
    #     resp = jsonify({'message': 'No file part in the request'})
    #     resp.status_code = 400
    #     return resp
    if request.files['file'] if 'file' in request.files else False:
        file = request.files['file']
    else:
        file = ''
    # if file.filename == '':
    #     resp = jsonify({'message': 'No file selected for uploading'})
    #     resp.status_code = 400
    #     return resp
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        filename = str(int(time.time() * 1000.0)) + '-' + filename
        data = json.loads(request.form['data'])
        item_args['name'] = data['name']
        item_args['shape'] = data['shape']
        item_args['color'] = data['color']
        item_args['owner'] = data['owner']
        item_args['date_found'] = data['date_found']
        item_args['location_found'] = data['location_found']
        item_args['file_name'] = filename
        item_obj = Items(**item_args)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        session.add(item_obj)
        session.commit()
        resp = jsonify({'message': 'File successfully uploaded'})
        resp.status_code = 201
        return resp
    elif file is not None:
        data = json.loads(request.form['data'])
        item_args['name'] = data['name']
        item_args['shape'] = data['shape']
        item_args['color'] = data['color']
        item_args['owner'] = data['owner']
        item_args['date_found'] = data['date_found']
        item_args['location_found'] = data['location_found']
        item_args['file_name'] = ''
        item_obj = Items(**item_args)
        session.add(item_obj)
        session.commit()
        resp = jsonify({'message': 'Data submitted successfully uploaded'})
        resp.status_code = 201
        return resp
    else:
        resp = jsonify({'message': 'Allowed file types are txt, pdf, png, jpg, jpeg, gif'})
        resp.status_code = 400
        return resp


app.run()
