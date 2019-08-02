from flask_restful import reqparse, Resource, Api
from flask import request, Flask,make_response 
import sys
import json
import datemtime
sys.path.append("..")
from thread_crawler import *

class GetCommit(Resource):
    def get(self):
        now = datetime.datetime.now()
        nowTime = now.strftime('%Y-%m-%d')
        e= test(nowTime)
        result = e.execute(8)
        return make_response(json.dumps(result, ensure_ascii=False))