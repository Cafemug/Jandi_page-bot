from flask import Flask
from flask_restful import Api
from flask_cors import CORS
from controller.get_commit import *
app = Flask(__name__)
CORS(app)
api = Api(app)


# api 라우팅 부분
api.add_resource(GetCommit, '/commit')


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")