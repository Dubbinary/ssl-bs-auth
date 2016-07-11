import requests, json, util.data_loader
from requests.auth import HTTPBasicAuth

#Iinitiatin variables for testing localhost server
def init_localhost_test():
    global host, url_get, url_post
    host = "localhost:5000"
    url_get = "http://%s/import" % host
    url_post = "http://%s/export" % host

#Iinitiatin variables for testing Heroku hosted server
def init_hosted_test():
    global host, url_get, url_post
    host = "ssl-bs-auth.herokuapp.com"
    url_get = "https://%s/import" % host
    url_post = "https://%s/export" % host

init_localhost_test()

#User and password for Basic HTTP Authentification
user = "admin"
password = "secret"


print "###################### TESTING GET REQUEST ######################"
res = requests.get(url_get, auth=HTTPBasicAuth(user, password))
print "RESPONSE STATUS CODE: ", res.status_code
print "JSON STATUS: "
try:
    #Try to get json from response
    json_data = res.json()

    #Saving .csv file
    util.data_loader.unload_data("csv_file.csv",json_data["csv"])

    #Saving html files
    htmls = json_data["htmls"]
    for id in htmls:
        util.data_loader.unload_data(id+".html",htmls[id])

    print "\t*OK: JSON RECIVED AND DATA SAVED FROM IT SUCCESSFULLY"
except ValueError:
    print "\t*WARNING: NO JSON IN RESPONSE"

##################################################################
print '\n'
##################################################################

print "###################### TESTING POST REQUEST ######################"
json_to_send = {'Key': 'Value here'}    #Test json to send on server

res = requests.post(url_post, data=json.dumps(json_to_send),auth=HTTPBasicAuth(user, password),headers={'Content-Type': 'application/json'})
print "RESPONSE STATUS CODE: ", res.status_code
print "RESPONSE TEXT: \n\t", res.text


