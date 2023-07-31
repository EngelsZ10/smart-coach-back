from flask import Flask,  Blueprint
from flask_cors import CORS
from controllers.auth import login
from controllers.addUsuario import addUsuario
from controllers.getFile import *
from controllers.uploadFile import upload_file_to_cpanel


app = Flask(__name__)

CORS(app, origins=["https://smartcoach.top", "127.0.0.1:3000"])


@app.route('/')
def index():
    return 'Hello  Flask!'


api = Blueprint('api', __name__)

api.route("/login")(login)
api.route("/addUsuario")(addUsuario)
api.route("/getFiles")(getFiles)
api.route("/uploadFile")(upload_file_to_cpanel)


app.register_blueprint(api, url_prefix='/')

if __name__ == '__main__':
    app.run(port=81)
