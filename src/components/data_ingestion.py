import os
import sys
from src.logger import logging
from src.exception import GemstoneException
from src.config.configuration import *

import pandas as pd
from sklearn.model_selection import train_test_split
from dataclasses import dataclass


@dataclass
class DataIngestionconfig:
    train_data_path:str=train_data_file_path
    test_data_path:str=test_data_file_path
    raw_data_path:str=raw_data_file_path
    
class DataIngestion:
    def __init__(self):
        self.ingestion_config = DataIngestionconfig()
         
    def initiate_data_ingestion(self):
        logging.info("="*50)
        logging.info("Data Ingestion Method Started")
        logging.info("="*50)

        try:
            df = pd.read_csv(data_file_path)
            logging.info("Dataset is readed")
            
            os.makedirs(os.path.dirname(self.ingestion_config.raw_data_path),
                        exist_ok=True)
            df.to_csv(self.ingestion_config.raw_data_path,index=False)
            logging.info(f"Raw data file path :[{self.ingestion_config.raw_data_path}]")
            
            logging.info("Train Test split started")
            train_set,test_set = train_test_split(df,test_size=0.30,random_state=42)
            
            train_set.to_csv(self.ingestion_config.train_data_path,index=False,header=True)
            test_set.to_csv(self.ingestion_config.test_data_path,index=False,header=True)
            
            logging.info("Ingestion of Data Completed")
            
            return(
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path
            )

        except Exception as e:
            logging.info('Exception occured at Data Ingestion stage')
            raise GemstoneException(e,sys)
        
if __name__ == "__main__":
    ing = DataIngestion()
    ing.initiate_data_ingestion()