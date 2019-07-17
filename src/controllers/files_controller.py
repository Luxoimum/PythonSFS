from flask import Flask, send_file
from flask_restful import Resource, Api
from src.services.upload import UploadFile as uf
import json, os.path


app = Flask(__name__)
api = Api(app)
SFSDir = '../../SFSDir/'
path = 'localhost:5000/images/'


class ImagesOperations (Resource):
    def get(self, name):
        if os.path.exists(SFSDir + name + '.png'):
            return send_file(SFSDir + name + '.png')
        elif os.path.exists(SFSDir + name + '.jpg'):
            return send_file(SFSDir + name + '.jpg')
        else:
            return 'El fichero no existe );', 404

    def post(self, img, name):
        uf.upload_file(json.loads(img), name)
        return '', 201


class Images (Resource):
    def get(self):
        files = []
        res = []
        # r=root, d=directories, f = files
        for r, d, f in os.walk(SFSDir):
            for file in f:
                files.append(path + os.path.join(r, file))

        for f in files:
            fil = f.replace(SFSDir, '')
            fil = fil.replace('.jpg', '')
            fil = fil.replace('.png', '')
            res.append(fil)

        return res


# Add resources with uri's associated to library


api.add_resource(Images, '/images')
api.add_resource(ImagesOperations, '/images/<name>')

if __name__ == '__main__':
    app.run(debug=True)