#-*- coding:utf-8 -*-
import requests
from bs4 import BeautifulSoup as bs
import time
from multiprocessing import Pool # Pool import하기
import datetime
from db_connect import mysql 
class test:
    def __init__(self,time):
        self.time=time
        self.session = requests.Session()
    def get_content(self,total):
        conn = mysql.connect()
        cursor = conn.cursor()
        data = total[1]
        nick = total[0]
        abs_link = 'https://github.com/'+data
        user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36'
        headers = {

    'User-Agent' : user_agent,
    "Cookie" : "tz=Asia%2FSeoul;"
}
        
        req = self.session.get(abs_link)
        req = requests.get(abs_link,headers=headers)
        html = req.text
        soup = bs(html, 'html.parser')
        a= soup.findAll('rect')
        resulta={}
        try:
            query = "update crawler set count = {count} where nickname = '{nickname}'".format(nickname=nick,count=a[-1]['data-count'])
            cursor.execute(query)
            _data = cursor.fetchall()
            if not _data:
                conn.commit()
                print({"update Success": 200})
            else:
                conn.rollback()
                print( {"update Failed": 404})
            # resulta["id"] = nick
            # resulta["value"] = a[-1]['data-count']
        except Exception as e:
            print(e) 
        cursor.close()
        conn.close()
        return resulta

    def register_content(self,total):
        conn = mysql.connect()
        cursor = conn.cursor()

        data = total[1]
        nick = total[0]
        abs_link = 'https://github.com/'+data
        user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36'
        headers = {

    'User-Agent' : user_agent,
    "Cookie" : "tz=Asia%2FSeoul;"
}
        
        req = self.session.get(abs_link)
        req = requests.get(abs_link,headers=headers)
        html = req.text
        soup = bs(html, 'html.parser')
        a= soup.findAll('rect')
        resulta={}
        try:
            query = "insert into crawler(nickname,count) values('{nickname}', {count})".format(nickname=nick,count=a[-1]['data-count'])
            cursor.execute(query)
            _data = cursor.fetchall()
            print(_data)
            if not _data:
                conn.commit()
                print({"Register Success": 200})
            else:
                conn.rollback()
                print( {"Register Failed": 404})
            # resulta["id"] = nick
            # resulta["value"] = a[-1]['data-count']
        except Exception as e:
            print(e) 
        cursor.close()
        conn.close()

        return resulta

    def execute(self,num):
        result=[]
        a={ '컴공돌이' : 'cafemug', '또르' : '9992', '복이' : 'changbokLee', '뇸뇸' : 'ellapresso', 'ㄷㄷ' : 'x86kernel', '뇌가딴딴' : 'ljhg1124', '싸이클러' : 'msnodeve', '1컴이' : 'horace-velmont', '레게힙합소년' : 'samkookji77', '방탕성현단' : 'seonghy', '해피스마일' : 'rnhappysmile', 'ccpo' : 'ccppoo', '깃토리' : 'haeyoonjo', '퐁퐁' : 'seongminseok', '깃별' : 'wg19', '맹코' : 'mengkko', '감동란' : 'th787706', '현' : 'kim6394', '개발냄새' : 'taewoo1991', 'joe' : 'porquelaquiero', '야옹' : 'asw91666', 'CLY' : 'dogcolley', '펭귄' : "cruisediary","sogo" : "sogoagain", "냐":"lilynys", "kstost":"kstost","나부랭이":"silverthreadk"}
        pool = Pool(processes=num) # 4개의 프로세스를 사용합니다.
        result.extend(pool.map(self.get_content, [(k,v) for k,v in a.items()]))# get_contetn 함수를 넣어줍시다.
        return(result)

if __name__ =="__main__":
    now = datetime.datetime.now()
    nowTime = now.strftime('%Y-%m-%d')
    e= test(nowTime)
    result = e.execute(2)
