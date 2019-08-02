from flask import Flask
from flask_restful import Api
from flask_cors import CORS
from flaskext.mysql import MySQL
# from controller.get_commit import *
import config

app = Flask(__name__)
CORS(app)
api = Api(app)

app.config['MYSQL_DATABASE_USER'] = config._DB_CONF['user']
app.config['MYSQL_DATABASE_PASSWORD'] = config._DB_CONF['passwd']
app.config['MYSQL_DATABASE_DB'] = config._DB_CONF['db']
app.config['MYSQL_DATABASE_HOST'] = config._DB_CONF['host']
app.config['MYSQL_DATABASE_PORT'] = config._DB_CONF['port']
mysql = MySQL()
mysql.init_app(app)
conn = mysql.connect()
cursor = conn.cursor()
# api 라우팅 부분
# api.add_resource(GetCommit, '/commit')


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")