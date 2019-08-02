from flask_restful import reqparse, Resource, Api
from flask import request, Flask,make_response 
import sys
import json
sys.path.append("..")
from db_connect import conn, cursor

class GetCommit(Resource):
    def get(self):
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
        return make_response(json.dumps(result, ensure_ascii=False))
