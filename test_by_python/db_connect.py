from flask_restful import reqparse, Resource, Api
from flask import request, Flask
from flaskext.mysql import MySQL
import config

app = Flask(__name__)
api = Api(app)

# MySQL 연결 세팅
app.config['MYSQL_DATABASE_USER'] = config._DB_CONF['user']
app.config['MYSQL_DATABASE_PASSWORD'] = config._DB_CONF['passwd']
app.config['MYSQL_DATABASE_DB'] = config._DB_CONF['db']
app.config['MYSQL_DATABASE_HOST'] = config._DB_CONF['host']
app.config['MYSQL_DATABASE_PORT'] = config._DB_CONF['port']

# MySQL 연결
mysql = MySQL()
mysql.init_app(app)
