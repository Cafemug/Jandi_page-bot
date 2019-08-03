from flask_restful import reqparse, Resource, Api
from flask import request, Flask,make_response 
import sys
import json
sys.path.append("..")
from db_connect import mysql

class GetNameCommit(Resource):
    def get(self, name):
        names = ['컴공돌이', '또르', '복이', '뇸뇸', 'ㄷㄷ', '뇌가딴딴', '싸이클러', '1컴이', '레게힙합소년', '방탕성현단', '해피스마일', 'ccpo', '깃토리', '퐁퐁', '깃별', '하준', '맹코', '감동란', '현', '개발냄새', 'GIT촙오', '야옹', '개입', '펭귄']
        if(not name in names):
            result = [{'result' : "Not Found name"}]
            return make_response(json.dumps(result, ensure_ascii=False))
        else:
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



