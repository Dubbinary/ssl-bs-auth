from flask import Flask, url_for, jsonify, request
from flask import render_template
from auth.basic_auth import requires_auth
import os
from functools import wraps
import util.data_loader

# from OpenSSL import SSL
# context = SSL.Context(SSL.SSLv23_METHOD)
# context.use_privatekey_file('keys/server.key')
# context.use_certificate_file('keys/server.crt')

app = Flask(__name__)

@app.route('/')
def getIndex():
    return render_template('index.html')

@app.route('/import', methods=['GET'])
@requires_auth
def do_import():
    print(request.headers)
    # test_json = {"project files": [f for f in os.listdir('.') if os.path.isfile(f)]}
    test_json = {
                "csv":  util.data_loader.load_data("data/test_projectsALL.csv"),
                "htmls": {"12438": util.data_loader.load_data("data/12438.html"),
                          "15270": util.data_loader.load_data("data/15270.html")},
                }
    return jsonify(**test_json)

@app.route('/export', methods=['GET','POST'])
@requires_auth
def do_export():
    if request.json:
        json=request.json
        return "got json Authorization: %s" % json.get("Authorization")
    else:
        return "On export link. NO JSON"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port='5000', debug=True)
15270