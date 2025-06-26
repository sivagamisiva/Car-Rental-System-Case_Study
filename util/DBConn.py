import mysql.connector
from util.DBProperty import get_property_string

def get_connection():
    try:
        props = get_property_string("db.properties")
        conn = mysql.connector.connect(
            host=props["host"],
            port=int(props["port"]),
            user=props["user"],
            password=props["password"],
            database=props["database"]
        )
        return conn
    except Exception as e:
        print("Error connecting to DB:", e)
        return None
