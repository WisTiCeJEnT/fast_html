from flask import Flask, request, jsonify
from fast_html import *
import json

app = Flask(__name__)

@app.route('/test')
def test():
    return "Working"

@app.route('/', methods=['GET', 'POST'])
def root():
    global code
    if request.method == 'POST':
        code = request.form['code']
    return code + FOOTER # + UPLOAD_LINK     #Hide Upload link

@app.route('/upload', methods=['GET'])
def upload():
    return UPLOAD_PAGE

@app.route('/code', methods=['GET'])
def code():
    return jsonify({"code": code})

code = ''

if __name__ == "__main__":
    app.run(debug = False,host="0.0.0.0", port=5000)
