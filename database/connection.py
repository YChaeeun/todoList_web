import pymysql

def get_connection():
    conn = pymysql.connect(host='127.0.0.1', user='guest', password='1234', db='todolist_db', charset='utf8')
    return conn

    