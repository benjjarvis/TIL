# -*- coding"utf-8 -*-
from flask import Flask, jsonify, render_template, request
from random import sample
import random
import requests

app = Flask(__name__)


# @app.route("/ide/<string:benjjarvis>/<string:workspace>")
# def benjjarvis_workspace(benjjarvis, workspace):
#     url="https://youtu.be/kiTni5eERoY"
#     return "<a href={}>내 영상!</a>".format(url)
#     a=print(webbrowser.open(url))
#     return "{}'s now watching {}!".format(benjjarvis, a)

#     return render_template(
#         'ide.html', 
#         name=benjjarvis, 
#         space=workspace)


@app.route("/ping")
def ping():
    return render_template('ping.html')


@app.route("/pong")
def pong():
    food = request.args.get('food')
    match_point = random.choice(range)

    

    MY_CHAT_ID = '798658564'
    BOT_TOKEN = '668815852:AAGncf4MrgoGtZYtxF47lM_XoAMDNKFJ2o4'
    msg = {{ food }}
    
    url = 'https://api.hphk.io/telegram/bot{}/sendMessage?chat_id={}&text={}'.format(BOT_TOKEN, MY_CHAT_ID, msg)
    
    res = requests.get(url)
    print(res.json())
    
    return render_template('pong.html', food=food, match_point=match_point)


@app.route("/")
def index():
    return render_template('choose_your_type.html')
    
    
@app.route("/type_A")
def type_A():
    return render_template('type_A.html')


@app.route("/type_B")
def type_B():
    return render_template('type_B.html')


# @app.route("/")
# def index(): 
#     lunch = random.choice(['20층','Diet'])
#     return render_template('index.html', lunch = lunch)
    
    
@app.route("/ide/<string:benjjarvis>/<string:workspace>")
def benjjarvis_workspace(benjjarvis, workspace):
    return "{}'s hot {}!".format(benjjarvis, workspace)    
    

@app.route("/hi")
def hi():
    return 'Hello SSAFY'
    
    
@app.route("/pick_lotto")
def pick_lotto():
    return jsonify(sample(range(1, 46), 6))
    
    
@app.route("/get_lotto")
def get_lotto():
    data={
        'numbers':[1, 2, 3, 4, 5, 6],
        'bonus':7
    }
    return jsonify(data)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8080)
    
