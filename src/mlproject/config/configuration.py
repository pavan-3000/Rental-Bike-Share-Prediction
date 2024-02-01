from src.mlproject.logger import logging
from src.mlproject.exception import CustomException
import sys

from src.mlproject.entity.config_entity import DataIngestionConfig,DataValidationConfig,DataTransformationConfig,ModelTrainerConfig,ModelEvalutionConfig
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
        
        
    def DataValidationManager(self) -> DataValidationConfig:
        config = self.config.data_validation
        schema = self.schema.COLUMNS_NAMES
        
        create_directory([config.root_dir])
        
        get_data_validation = DataValidationConfig(        
            root_dir = config.root_dir,
            data_path = config.data_path,
            STATUS_INFO = config.STATUS_INFO,
            all_schema = schema
        )
        
        return get_data_validation
    
    
    def DataTransformationManager(self) -> DataTransformationConfig:
        try:
            
            
            config = self.config.data_transformation
        
            create_directory([config.root_dir])
        
            logging.info("created root directory")
            
            
            get_data_transformation = DataTransformationConfig(
                root_dir=config.root_dir,
                data_path=config.data_path
            )
            
            
            return get_data_transformation
        
        except Exception as e:
            raise CustomException(e,sys)
        
    def ModelTrainerManager(self) -> ModelTrainerConfig:
        try:
            config = self.config.model_trainer
            schema = self.schema.TARGET_NAME
            
            create_directory([config.root_dir])
            
            get_model_trainer = ModelTrainerConfig(
                root_dir=config.root_dir,
                train_data_path=config.train_data_path,
                test_data_path=config.test_data_path,
                model_name=config.model_name,
                TARGET_NAME = schema.name
            )
            
            
            return get_model_trainer
            
            
            
            
        except Exception as e:
            raise CustomException(e,sys)
        
        
    def ModelEvalutionManager(self) -> ModelEvalutionConfig:
        try:
            config = self.config.model_evalution
            schema  = self.schema.TARGET_NAME
            
            create_directory([config.root_dir])
            
            get_model_evalution = ModelEvalutionConfig(
                root_dir=config.root_dir,
                test_data_path=config.test_data_path,
                model_path=config.model_path,
                metric_file_name=config.metric_file_name,
                target_name=schema.name
            )
            
            return get_model_evalution
            
        except Exception as e:
            raise CustomException(e,sys)