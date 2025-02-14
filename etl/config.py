import logging

# Define log file
LOG_FILE = 'etl_pipeline.log'

logging.basicConfig(
    filename=LOG_FILE,
    level=logging.INFO,
    format= "%(asctime)s - %(levelname)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S"
)

# database configurations
DB_CONFIG = {
    'dbname' : 'investment_db',
    'user' : 'postgres',
    'password' : '1234',
    'host': 'localhost',
    'port': 5432
}