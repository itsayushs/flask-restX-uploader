from flask import Flask
from flask_restx import Resource, Api, fields
import werkzeug
from werkzeug.utils import secure_filename
from flask_restx import reqparse
import os

app = Flask(__name__)
api = Api(app,version='0.1', title='CodeEngine-UserRequest')
model = api.model('userdata', {
    'username': fields.String,
    'task_number': fields.String,
    'language': fields.String,
    'file_path': fields.String,
})
file_upload = reqparse.RequestParser()
file_upload.add_argument('doc1',
                         type=werkzeug.datastructures.FileStorage, 
                         location='files', 
                         required=True, 
                         help='Document 1')

app.config['Upload_folder'] = './upload/'

@api.route('/upload/')
class my_file_upload(Resource):
    @api.expect(file_upload)
    def post(self):
        args = file_upload.parse_args()
        args['doc1'].save(os.path.join(app.config['Upload_folder'],secure_filename(args['doc1'].filename)))
        a = args['doc1']
        print(a)
        return {'status': 'Done'}


if __name__ == '__main__':
    app.run(debug=True)