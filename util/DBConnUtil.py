import mysql.connector
import os
from util.DBPropertyUtil import get_property_string
def get_connection():
    try:
        project_root = os.path.dirname(os.path.dirname(__file__))
        properties_path = os.path.join(project_root, 'db.properties')

        with open(properties_path, 'r') as f:
            props = dict(line.strip().split('=') for line in f if '=' in line)
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
