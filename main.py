from flask import Flask, url_for, jsonify
from flask import render_template
from auth.basic_auth import requires_auth
import os
app = Flask(__name__)

@app.route('/')
def getIndex():
    return render_template('index.html')

@app.route('/import/', methods=['GET'])
@requires_auth
def do_import():
    test_json = {"project files": [f for f in os.listdir('.') if os.path.isfile(f)] }
    return jsonify(**test_json)

@app.route('/export/', methods=['GET','POST'])
@requires_auth
def do_export():
    return "On export link"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port='5000')
