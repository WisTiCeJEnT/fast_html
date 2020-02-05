from flask import Flask, request
from fast_html import *

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

code = ''

if __name__ == "__main__":
    app.run(debug = False,host="0.0.0.0", port=5000)
