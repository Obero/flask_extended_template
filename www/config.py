import os

DEBUG = True

HOST = '127.0.0.1'
PORT = 5030
SECRET_KEY = os.urandom(24).encode('hex')

# SQLALCHEMY_DATABASE_URI = "sqlite+pysqlite:///db_name.sqlite"
# SQLALCHEMY_DATABASE_URI = "mysql://user:password@localhost/db_name?charset=utf8"
