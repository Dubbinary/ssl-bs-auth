import base64

#Function which reads file and encodes it to base64
# for proper integration in json and further sending
def load_data(path):
    with open(path, 'rb') as data:
        data = data.read()
        return base64.encodestring(data)

#Function which decodes data from base64
def unload_data(path, data):
    with open(path, 'wb') as file:
        file.write(base64.decodestring(data))


