from flask import Flask
from mysql.connector import MySQLConnection
import mysql

app = Flask(__name__)
app.secret_key = 'teste'
        
app.config.from_pyfile('config.py')

conexao: mysql = app.config['CONEXAO']

from views import *

if __name__ == '__main__':
    app.run(debug=True)