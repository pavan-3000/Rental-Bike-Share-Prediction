from src.mlproject.logger import logging
from src.mlproject.exception import CustomException
import sys

from src.mlproject.entity.config_entity import DataIngestionConfig
from src.mlproject.constants import *

from src.mlproject.utils.common import read_yaml,create_directory


class ConfigManager:
    def __init__(
        self,
        config_path=CONFIG_FILE_PATH,
        params_path = PARAMS_FILE_PATH,
        schema_path= SCHEMA_FILE_PATH
    ):
        self.config = read_yaml(config_path)
        self.params = read_yaml(params_path)
        self.schema = read_yaml(schema_path)
        
        logging.info("read the yaml file")
        
        create_directory([self.config.artifacts_root])
        
        logging.info("root directory is created")
        
    
    def DataIngestionManager(self) -> DataIngestionConfig:
        try:
            config = self.config.data_ingestion
            
            create_directory([config.root_dir])
            
            logging.info("created data ingestion artifacts")
            
            get_data_ingestion = DataIngestionConfig(
                root_dir=config.root_dir,
                source_URL=config.source_URL,
                local_data_file=config.local_data_file,
                unzip_path=config.unzip_data
            )
            
            return get_data_ingestion
            
            
            
            
        except Exception as e:
            raise CustomException(e,sys)