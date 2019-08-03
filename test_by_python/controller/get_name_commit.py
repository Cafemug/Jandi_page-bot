from flask_restful import reqparse, Resource, Api
from flask import request, Flask,make_response 
import sys
import json
sys.path.append("..")
from db_connect import mysql

class GetNameCommit(Resource):
    def get(self, name):
        conn = mysql.connect()
        cursor = conn.cursor()
        query = "select * from crawler where nickname ='{name}'".format(name=name)
        cursor.execute(query)
        data = cursor.fetchone()
        result =[]
        temp ={}
        temp["id"]=data[0]
        temp["value"]= data[1]
        print(temp)
        result.append(temp)
        print(result)
        cursor.close()
        conn.close()
        return make_response(json.dumps(result, ensure_ascii=False))



