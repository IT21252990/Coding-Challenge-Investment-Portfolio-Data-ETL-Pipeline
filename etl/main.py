from extractor import extract_data_from_csv
from transformer import transform_data_in_python
from loader import upload_data_to_sql
import logging

HOLDINGS_DATA_1 = '../data/holdings_data_1.csv'
HOLDINGS_DATA_2 = '../data/holdings_data_2.csv'
PORTFOLIO_STATS_1 = '../data/portfolio_stats_1.csv'
PORTFOLIO_STATS_2 = '../data/portfolio_stats_2.csv'

csv_files = {
    "holding": [HOLDINGS_DATA_1 , HOLDINGS_DATA_2],
    "portfolio_stats": [PORTFOLIO_STATS_1 , PORTFOLIO_STATS_2]
}

try:
    logging.info("Starting ETL pipeline...")

    for file in csv_files['holding']:
        df = extract_data_from_csv(file)
        transformed_df = transform_data_in_python(df , 'holding')
        upload_data_to_sql(transformed_df , "holdings_staging")

    for file in csv_files['portfolio_stats']:
        df = extract_data_from_csv(file)
        transformed_df = transform_data_in_python(df , 'portfolio_stats')
        upload_data_to_sql(transformed_df , "portfolio_stats_staging")

    logging.info("ETL pipeline was ran successfully...")
except Exception as e:
    logging.error(f"Error while running ETL pipeline ... : {e}")