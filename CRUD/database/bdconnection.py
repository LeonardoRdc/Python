import mysql.connector

def conectar():
    return mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = '42866824mar.',
    database = 'bdfirst',
)