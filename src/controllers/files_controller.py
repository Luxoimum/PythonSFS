from flask import Flask, send_file
from flask_restful import Resource, Api
from src.services.upload import UploadFile as uf
import json


app = Flask(__name__)
api = Api(app)


# Upload an image into the server


class Upload (Resource):
    def post(self, img, name):
        uf.upload_file(json.loads(img), name)
        return '', 201


# Download an image


class Download (Resource):
    def get(self, name):
        return send_file('../../SFSDir/'+name)


# Add resources with uri's associated to library


api.add_resource(Upload, '/upload/<name>')
api.add_resource(Download, '/download/<name>')

if __name__ == '__main__':
    app.run(debug=True)