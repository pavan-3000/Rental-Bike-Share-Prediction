from src.mlproject.logger import logging
from src.mlproject.exception import CustomException
import sys

from src.mlproject.entity.config_entity import DataValidationConfig
from src.mlproject.config.configuration import ConfigManager

from src.mlproject.components.data_valdation import DataValidation


class DataValidationPipeline:
    def __init__(self):
        pass
    
    
    def main(self):
        try:
            logging.info('stage 2 has stared')
            
            valid_config = ConfigManager()
            valid_config = valid_config.DataValidationManager()
            
            data_validation = DataValidation(config=valid_config)
            data_validation.validate_all_col()
            
            logging.info("stagee 2 has commpleted")
            
            
        except Exception as e:
            raise CustomException(e,sys)
        
    