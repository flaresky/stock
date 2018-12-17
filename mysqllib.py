import settings
import mysql.connector

def get_connection():
    return mysql.connector.connect(**settings.mysqlConfig)

def run_sql(sql):
    cnx = get_connection()
    cursor = cnx.cursor()
    cursor.execute(sql)
    cnx.commit()
    cursor.close()
    cnx.close()

def fetch(sql):
    cnx = get_connection()
    cursor = cnx.cursor(dictionary=True)
    cursor.execute(sql)
    res  = cursor.fetchall()
    cursor.close()
    cnx.close()
    return res

def fetch_one(sql):
    res = fetch(sql)
    if len(res) == 0:
        return None
    return res[0]