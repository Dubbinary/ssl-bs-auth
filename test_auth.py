import requests
from requests.auth import HTTPBasicAuth
import json

# host = "localhost"
host = "ssl-bs-auth.herokuapp.com"
url_get = "https://%s:5000/import" % host
url_post = "https://%s:5000/export" % host

user = "admin"
password = "secret"

headers = {'Authorization': 'Basic YWRtaW46c2VjcmV0'}   ##Scrapped auth

res = requests.get(url_get, auth=HTTPBasicAuth(user, password), verify='keys/server.crt')
print "Status: ",res.status_code
print "Text: ",res.text
try:
    print "Json: ",res.json()
except ValueError:
    print "NO JSON IN RESPONSE"

res = requests.post(url_post, data=json.dumps(headers),auth=HTTPBasicAuth(user, password),headers={'Content-Type': 'application/json'})
print "Status: ",res.status_code
print "Text: ",res.text
try:
    print "Json: ",res.json()
except ValueError:
    print "NO JSON IN RESPONSE"
