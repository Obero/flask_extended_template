__author__ = 'Obero'

import config
from flask_extended_template import app

if __name__ == '__main__':
    print '[Config] Host : ', config.HOST
    print '[Config] Port : ', config.PORT
    print '[Config] Debug : ', config.DEBUG
    app.run(debug=config.DEBUG, host=config.HOST, port=config.PORT)
