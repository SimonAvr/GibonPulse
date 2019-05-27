from flask import Flask, jsonify,json

app = Flask(__name__)


@app.route('/pulse', methods=['POST','GET'])
def postJsonHandler():
    f = open('data.txt', "r")
    lines = f.readlines()
    json = {"status": (lines[0]).replace('\n', ''),
            "heart_rate": (lines[1]).replace('\n', ''),
            "head_positions": (lines[2]).replace('\n', ''),
            "forehead_position": (lines[3]).replace('\n', ''),
            "fps": (lines[4]).replace('\n', '')}  # this is a dict object, python equivalent to js object
    f.close()
    return jsonify(json)

app.run()