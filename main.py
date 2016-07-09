from flask import Flask, url_for
from flask import render_template
app = Flask(__name__)

@app.route('/')
def getIndex():
    return render_template('index.html')

@app.route('/import/', methods=['GET'])
def do_import():
    return "On import link"

@app.route('/export/', methods=['POST'])
def do_export():
    return "On export link"

if __name__ == "__main__":
    application.run(host='0.0.0.0')
    
