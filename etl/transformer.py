import pandas as pd
import numpy as np
import logging

def transform_data_in_python(df , file_type):

    try:
        logging.info(f"Transforming {file_type} data...")
        # convert all columns in df in to lowercase and remove white spaces
        df.columns = df.columns.str.strip().str.lower()

        # list the numeric columns
        numeric_columns = ['quantity' , 'market_value' , 'nav','daily_pnl','ytd_return','sharpe_ratio','volatility','var_95' ]

        for col in numeric_columns:
            if col in df.columns:
                df[col] = df[col].astype(str) # convert as the string before cleaning
                df[col] = df[col].str.replace(',' , '' , regex=True) # remove the commas in the column values
                df[col] = df[col].str.replace('%' , '' , regex=True) # remove the percentage sign in the column values
                df[col] = pd.to_numeric(df[col] , errors="coerce") # convert column values in to numeric , NaN if occur any error

        # convert different formats dates into one format
        df['business_date'] = pd.to_datetime(df['business_date'], errors='coerce')

        # Handle missing values
        df.fillna(np.nan , inplace=True)
        logging.info(f"Successfully Transformed {file_type} data... with {len(df)}")
        return df
    except Exception as e:
        logging.error(f"Error while transforming data in {file_type} : {e}")
        return None
