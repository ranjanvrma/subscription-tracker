import mysql.connector

def get_connection():
    return mysql.connector.connect(
        host = 'localhost',
        user = 'root',
        password = 'Verma@2310',
        database = "subscription_tracker"
    )