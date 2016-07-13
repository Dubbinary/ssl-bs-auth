import requests, json, util.data_loader
from requests.auth import HTTPBasicAuth

#Iinitiatin variables for testing localhost server
def init_localhost_test():
    global host, url_import, url_export, url_generate
    host = "localhost:5000"
    url_import = "http://%s/import" % host
    url_export = "http://%s/export" % host
    url_generate = "http://%s/generate" % host

#Iinitiatin variables for testing Heroku hosted server
def init_hosted_test():
    global host, url_import, url_export, url_generate
    host = "ssl-bs-auth.herokuapp.com"
    url_import = "https://%s/import" % host
    url_export = "https://%s/export" % host
    url_generate = "https://%s/generate" % host

# init_hosted_test()
init_localhost_test()

#User and password for Basic HTTP Authentification
user = "admin"
password = "secret"


print "###################### TESTING GENERATE LINK ######################"
res = requests.get(url_generate, auth=HTTPBasicAuth(user, password))
print "RESPONSE STATUS CODE: ", res.status_code
print "JSON STATUS: "
try:
    #Try to get json from response
    generate_json = res.json()

    #Saving .csv file
    util.data_loader.unload_data("csv_file.csv", generate_json["csv"])

    #Saving html files
    htmls = generate_json["htmls"]
    for id in htmls:
        util.data_loader.unload_data(id+".html",htmls[id])

    print "\t*OK: GENERATE JSON RECIVED AND DATA SAVED FROM IT SUCCESSFULLY"
except ValueError:
    print "\t*WARNING: NO JSON IN RESPONSE"

##################################################################
print '\n'
##################################################################

print "###################### TESTING IMPORT LINK ######################"
res = requests.get(url_import, auth=HTTPBasicAuth(user, password))
print "RESPONSE STATUS CODE: ", res.status_code
print "JSON STATUS: "
try:
    import_json = res.json()
    print "\t*OK: IMPORT JSON RECIVED SUCCESSFULLY"
    print import_json
except ValueError:
    print "\t*WARNING: NO JSON IN RESPONSE"

##################################################################
print '\n'
##################################################################

print "###################### TESTING EXPORT LINK ######################"
json_to_send = {'Key': 'Value here'}    #Test json to send on server

res = requests.post(url_export, data=json.dumps(json_to_send),auth=HTTPBasicAuth(user, password),headers={'Content-Type': 'application/json'})
print "RESPONSE STATUS CODE: ", res.status_code
print "RESPONSE TEXT: \n\t", res.text
