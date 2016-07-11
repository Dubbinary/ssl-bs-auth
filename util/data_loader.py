import base64
def load_data(path):
    with open(path, 'rb') as data:
        data = data.read()
        return base64.encodestring(data)


def unload_data(path, data):
    with open(path, 'wb') as file:
        file.write(base64.decodestring(data))


