from flask import Flask,  Blueprint
from controllers.auth import login


app = Flask(__name__)

@app.after_request 
def after_request(response):
    header = response.headers
    header['Access-Control-Allow-Origin'] = '*'
    # Other headers can be added here if needed
    return response

@app.route('/')
def index():
    return 'Hello  Flask!'

@app.route('/prueba')
def prueba():
    return 'Hello  Prueba!'


api = Blueprint('api', __name__)

api.route("/login")(login)


app.register_blueprint(api, url_prefix='/')

if __name__ == '__main__':
    app.run()
