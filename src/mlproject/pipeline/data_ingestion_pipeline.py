from src.mlproject.logger import logging
from src.mlproject.exception import CustomException
import sys
from src.mlproject.entity.config_entity import DataIngestionConfig
from src.mlproject.config.configuration import ConfigManager
from src.mlproject.components.data_ingestion import DataIngestion


class DataIngestionPipeline:
    def __init__(self):
        pass
    
    
    
    def main(self):
        try:
            
            logging.info("stage 1 started")
            
            ingestion_config = ConfigManager()
            config_ing = ingestion_config.DataIngestionManager()
            data_ingestion = DataIngestion(config=config_ing)
            data_ingestion.download_zip_file()
            data_ingestion.unzip_file()
            
            logging.info("level 1 completed without error")
            
            
            
        except Exception as e:
            raise CustomException(e,sys)