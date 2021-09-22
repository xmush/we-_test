import hashlib
from blueprints import app

salt = app.config['APP_KEY'] 

class Encryption :
    def __init__(self):
        pass

    def generatePassword(plaintext) :
        encoded = ('%s%s' % (plaintext, salt)).encode('utf-8')
        chipertext = hashlib.sha512(encoded).hexdigest()

        return chipertext 

