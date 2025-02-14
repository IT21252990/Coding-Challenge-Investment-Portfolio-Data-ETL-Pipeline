import psycopg2
from config import DB_CONFIG
import logging

def get_db_connection():
    try:
        logging.info("Connecting the DB..")
        conn = psycopg2.connect(**DB_CONFIG)
        return conn
    except Exception as e:
        logging.error(f"Error occur while connecting to DB : {e}")