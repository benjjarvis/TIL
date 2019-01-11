import random
from flask import Flask, jsonify # 리스트를 세상 밖으로 보여주는 애

app = Flask(__name__)

@app.route('/') # decorator 꾸며주는애
def index():
    return 'Hi, I am JISS'

@app.route('/ssafy')
def ssafy():
    return 'ssafy'

@app.route('/hi/<string:name>')
def hi(name):
    return(f'hi {name}!')

@app.route('/pick_lotto')
def pick_lotto():
    numbers = random.sample(range(1, 46),6)
    return jsonify(numbers)

if __name__ == '__main__':
    app.run(debug=True) # 서버 일해..

