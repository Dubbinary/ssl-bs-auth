from flask import Flask, jsonify, request, render_template
from auth.basic_auth import requires_auth
import util.data_loader

#Create Flask app instance
app = Flask(__name__)

#Resolving index url
@app.route('/')
def getIndex():
    return render_template('index.html')

#Resolving request to send data with which model
#would be generated
@app.route('/generate', methods=['GET'])
@requires_auth  #Requires Basic HTTP Authentication
def do_generate():

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
    generetion_json = {
                "csv":  util.data_loader.load_data("data/test_projectsALL.csv"),
                "htmls": {"12438": util.data_loader.load_data("data/12438.html"),
                          "15270": util.data_loader.load_data("data/15270.html"),
                          "13355": util.data_loader.load_data("data/13355.html"),
                          "13356": util.data_loader.load_data("data/13356.html"),
                          "13358": util.data_loader.load_data("data/13358.html"),
                          "13359": util.data_loader.load_data("data/13359.html"),
                          "13360": util.data_loader.load_data("data/13360.html"),
                          "13361": util.data_loader.load_data("data/13361.html"),
                          "13363": util.data_loader.load_data("data/13363.html"),
                          "13364": util.data_loader.load_data("data/13364.html"),
                          "13365": util.data_loader.load_data("data/13365.html"),
                          "13371": util.data_loader.load_data("data/13371.html"),
                          "13372": util.data_loader.load_data("data/13372.html")}
                }
    return jsonify(**generetion_json)

#resolving request to get import data
@app.route('/import', methods=['GET'])
@requires_auth
def do_import():
    import_json = {
        "13355": util.data_loader.load_data("data/13355.html"),
        "13356": util.data_loader.load_data("data/13356.html"),
        "13358": util.data_loader.load_data("data/13358.html"),
        "13359": util.data_loader.load_data("data/13359.html"),
        "13360": util.data_loader.load_data("data/13360.html"),
        "13361": util.data_loader.load_data("data/13361.html"),
        "13363": util.data_loader.load_data("data/13363.html"),
        "13364": util.data_loader.load_data("data/13364.html"),
        "13365": util.data_loader.load_data("data/13365.html"),
        "13371": util.data_loader.load_data("data/13371.html"),
        "13372": util.data_loader.load_data("data/13372.html"),
    }
    return jsonify(**import_json)

#Resolving request to receive prediction result
@app.route('/export', methods=['POST'])
@requires_auth
def do_export():
    if request.json:
        resiveed_json = request.json
        return "*OK: JSON HAS BEEN RECEIVED ON SERVER: %s" % resiveed_json
    else:
        return "*WARNING: NO JSON RECEIVED ON SERVER"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port='5000', debug=True)
