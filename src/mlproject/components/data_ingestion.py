from src.mlproject.logger import logging
from src.mlproject.exception import CustomException
import sys
from src.mlproject.entity.config_entity import DataIngestionConfig
from src.mlproject.config.configuration import ConfigManager

import gdown
import zipfile
import os



class DataIngestion:
    def __init__(self,config:DataIngestionConfig):
        self.config = config
        
        
    def download_zip_file(self):
        
        try:
            
            data = self.config.source_URL
            download_path = self.config.local_data_file
            os.makedirs("artifacts/data_ingestion",exist_ok=True)
            
            logging.info("downliad source and save at dodwnlaid p0ath")
            
            
            file_id = data.split('/')[-2]
            preile = 'https://drive.google.com/uc?export=download&id='
            
            gdown.download(preile+file_id,download_path)
            logging.info("downliading is compleed")

        except Exception as e:
            raise CustomException(e,sys)
        
        
        
    def unzip_file(self):
        try:
            unzip_path = self.config.unzip_path
            os.makedirs(unzip_path,exist_ok=True)
            
            with zipfile.ZipFile(self.config.local_data_file,'r') as f:
                f.extractall(unzip_path)
                
            logging.info('unzip file is successfully completed')
            
            
            
            
        except Exception as e:
            raise CustomException(e,sys)