from flask import Flask
from flask_restful import Api
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
api = Api(app)


# api 라우팅 부분
from controller.get_commit import *
from controller.get_name_commit import *
api.add_resource(GetCommit, '/commit')
api.add_resource(GetNameCommit, '/com/<name>')

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")