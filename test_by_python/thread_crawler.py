# parser.py
import requests
from bs4 import BeautifulSoup as bs
import time
from multiprocessing import Pool # Pool import하기


def get_links(): # 블로그의 게시글 링크들을 가져옵니다.
    data = ["cafemug","9992","changbokLee","ellapresso","x86kernel","lihj1124","msnodeve","horace-velmont","samkookji77","seonghy","rnhappysmile","ccppoo","haeyoonjo","seongminseok","wg19","mengkko","th787706","apple-143","porquelaquiero","asw91666","norikim"]
    nick = ["컴공돌이","또르","복이","뇸뇸","ㄷㄷ","뇌가딴딴","싸이클러","1컴이","레게힙합소년","방탕성현단","해피스마일","ccpo","깃토리","퐁퐁","깃별","하준","맹코","감동란","현","개발냄새","GIT촙오","야옹","개입"]
    return data

def get_content(link):
    abs_link = 'https://github.com/'+link
    req = requests.get(abs_link)
    html = req.text
    soup = bs(html, 'html.parser')
    a= soup.findAll('rect')
    a.reverse()
    for i in a:
        if i['data-date'] == "2019-08-01":
            print(i['data-count'])
            return 

if __name__=='__main__':
    start_time = time.time()
    # data = ["cafemug","9992","changbokLee","ellapresso","x86kernel","lihj1124","msnodeve","horace-velmont","samkookji77","seonghy","rnhappysmile","ccppoo","haeyoonjo","seongminseok","wg19","mengkko","th787706","apple-143","porquelaquiero","asw91666","norikim"]
    # for i in data:
    #     get_content(i)
    pool = Pool(processes=6) # 4개의 프로세스를 사용합니다.
    pool.map(get_content, get_links()) # get_contetn 함수를 넣어줍시다.
    print("--- %s seconds ---" % (time.time() - start_time))