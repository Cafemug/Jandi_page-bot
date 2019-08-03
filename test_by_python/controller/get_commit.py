from flask_restful import reqparse, Resource, Api
from flask import request, Flask,make_response 
import sys
import json
sys.path.append("..")
from db_connect import mysql

class GetCommit(Resource):
    def get(self):
        conn = mysql.connect()
        cursor = conn.cursor()
        query = "select * from crawler"
        cursor.execute(query)
        data = cursor.fetchall()
        result =[]
        for item in data:
            temp ={}
            temp["id"]=item[0]
            temp["value"]= item[1]
            print(temp)
            result.append(temp)
        print(result)
        cursor.close()
        conn.close()
        return make_response(json.dumps(result, ensure_ascii=False))
