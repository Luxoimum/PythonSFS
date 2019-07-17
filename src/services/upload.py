from PIL import Image
from io import BytesIO
import base64
import pickle


class UploadFile:
    @staticmethod
    def upload_file(img, name):
        img_data = base64.b64decode(img['img'])
        img_data = pickle.loads(img_data)
        img = Image.open(BytesIO(img_data))
        img.save('SFSDir/' + name)
