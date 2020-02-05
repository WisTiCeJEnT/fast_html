from flask import Flask, request
import os

app = Flask(__name__)

@app.route('/test')
def test():
    return "Working"

@app.route('/', methods=['GET', 'POST'])
def root():
    global code
    if request.method == 'POST':
        code = request.form['code']
    return code

@app.route('/upload', methods=['GET'])
def upload():
    return UPLOAD_PAGE

UPLOAD_PAGE = f"""
<html>
    <form action="{os.environ['URL']}/" method="post">
        <input type="text" name="code">
        <input type="submit" value="Deploy ~">
    </form>
</html>
"""
print(f"""URL = {os.environ['URL']}/""")

if __name__ == "__main__":
    app.run(debug = False,host="0.0.0.0", port=5000)
