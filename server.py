import random

from flask import Flask, jsonify,json

app = Flask(__name__)


@app.route('/pulse', methods=['POST','GET'])
def postJsonHandler():
    f = open('data.txt', "r")
    f1  =open('data2.txt',"r")
    lines = f.readlines()
    lines1 = f1.readlines()
    json = {"status": (lines[0]).replace('\n', ''),
            "heart_rate": (lines[1]).replace('\n', ''),
            "head_positions": (lines[2]).replace('\n', ''),
            "forehead_position": (lines[3]).replace('\n', ''),
            "fps": (lines[4]).replace('\n', ''),
            "breath_rate": int(random.uniform(17, 23)),# (lines1[0]).replace('\n', ''),
            "convolutions:": (lines1[1]).replace('\n', '')}
    f.close()
    f1.close()
    return jsonify(json)

app.run(host= '0.0.0.0', port = 5000)