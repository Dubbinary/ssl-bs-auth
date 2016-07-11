import requests
from requests.auth import HTTPBasicAuth
import json, util.data_loader

# host = "localhost:5000"
host = "ssl-bs-auth.herokuapp.com"
url_get = "https://%s/import" % host
url_post = "https://%s/export" % host

user = "admin"
password = "secret"

headers = {'Authorization': 'Basic YWRtaW46c2VjcmV0'}   ##Scrapped auth

res = requests.get(url_get, auth=HTTPBasicAuth(user, password))
print "Status: ",res.status_code
print "Status: ",res.headers
# print "Text: ",res.text
try:
    json_data = res.json()
    #Save .csv file
    util.data_loader.unload_data("csv_file.csv",json_data["csv"])
    #Save htmls
    htmls = json_data["htmls"]
    for id in htmls:
        util.data_loader.unload_data(id+".html",htmls[id])
except ValueError:
    print "NO JSON IN RESPONSE"

print "@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"

res = requests.post(url_post, data=json.dumps(headers),auth=HTTPBasicAuth(user, password),headers={'Content-Type': 'application/json'})
print "Status: ",res.status_code
print "Status: ",res.headers
print "Text: ",res.text
try:
    print "Json: ",res.json()
except ValueError:
    print "NO JSON IN RESPONSE"
