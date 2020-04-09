#https://daewonyoon.tistory.com/295 참조#

import sys
sys.path.append('C:\\Users\\hyund\\AppData\\Local\\Programs\\Python\\Python36\\Lib\\site-packages')

from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World'

if __name__ == '__main__':  #해당 모듈이 import되지 않고 실행되는 메인 위치인지 확인
    app.run()