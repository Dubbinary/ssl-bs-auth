from flask import Flask, jsonify, request, render_template
from auth.basic_auth import requires_auth
import util.data_loader

#Create Flask app instance
app = Flask(__name__)

#Resolving index url
@app.route('/')
def getIndex():
    return render_template('index.html')

#Resolving import url with GET method
@app.route('/import', methods=['GET'])
@requires_auth  #Requires Basic HTTP Authentication
def do_import():

    #Building json with required data for ML module
    #
    #Basic structure of json
    #{
    #   "csv": "<encoded_csv>",
    #   "htmls": {
    #       "<id>": "<encoded_html>",
    #       "<id>": "<encoded_html>"
    #   }
    #}
    test_json = {
                "csv":  util.data_loader.load_data("data/test_projectsALL.csv"),
                "htmls": {"12438": util.data_loader.load_data("data/12438.html"),
                          "15270": util.data_loader.load_data("data/15270.html")},
                }
    return jsonify(**test_json)

#Resolving import url with POST method
@app.route('/export', methods=['POST'])
@requires_auth
def do_export():
    if request.json:
        resiveed_json = request.json
        return "*OK: JSON HAS BEEN RESIVED ON SERVER: %s" % resiveed_json
    else:
        return "*WARNING: NO JSON RESIVED ON SERVER"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port='5000', debug=True)