import pandas as pd
import logging

def extract_data_from_csv(file_path):
    try:
        logging.info(f"Extracting data from {file_path}")
        df = pd.read_csv(file_path)
        logging.info(f"Data Extracted successfully from {file_path}")
        return df
    except Exception as e:
        logging.error(f"Error while extracting data from {file_path} : {e}")
        return None