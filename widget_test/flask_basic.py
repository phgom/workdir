#https://daewonyoon.tistory.com/295 참조#

import sys
sys.path.append('C:\\Users\\hyund\\AppData\\Local\\Programs\\Python\\Python36\\Lib\\site-packages')

from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
    page_title="플라스크 테스트"
    return render_template("index.html", mytitle=page_title, mycontent="Hello World")
# def hello_world():
#     return 'Hello World'

@app.route('/test')
def hello_world2():
    return render_template("temp-plot.html")

if __name__ == '__main__':  #해당 모듈이 import되지 않고 실행되는 메인 위치인지 확인
    app.run()