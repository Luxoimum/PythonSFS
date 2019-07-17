from PIL import Image
import base64
import pickle


class DownloadFile:
    @staticmethod
    def get_file(name):
        img = Image.open('SFSDir/' + name)
        img_data = pickle.dumps(img)

        return base64.b64encode(img_data).decode('utf-8')
