import pandas as pd
from database import get_db_connection
import logging

def upload_data_to_sql(df , table_name):

    try:
        logging.info(f"Inserting data in to {table_name}")
        # get the connection
        conn = get_db_connection()

        cursor = conn.cursor()

        columns = ', '.join(df.columns)
        values = ', '.join(['%s'] * len(df.columns))

        insert_query = f"INSERT INTO {table_name} ({columns}) VALUES ({values})"


        for _, row in df.iterrows():
            row = [None if pd.isna(x) else x for x in row]
            cursor.execute(insert_query , tuple(row))
        
        conn.commit()
        logging.info(f"Data Inserted successfully for the {table_name}")
    except Exception as e:
        logging.error(f"Error with Inserting data to {table_name} : {e}")
        raise
    finally:
        cursor.close()
        conn.close()
