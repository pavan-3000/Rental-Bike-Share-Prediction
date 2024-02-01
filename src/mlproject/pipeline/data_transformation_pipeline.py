from src.mlproject.logger import logging
from src.mlproject.exception import CustomException
import sys

from src.mlproject.entity.config_entity import DataTransformationConfig
from src.mlproject.config.configuration import ConfigManager

from src.mlproject.components.data_transformation import DataTransformation


class DataTransformationPipeline:
    def __init__(self):
        pass
    
    def main(self):
        try:
            logging.info("stage 3 has started")
            
            trans_config = ConfigManager()
            trans_config = trans_config.DataTransformationManager()
            
            data_transform  = DataTransformation(config = trans_config)
            
            data_transform.get_data_transformation()
                
            logging.info("stage 3 has completd sucessfully")
            
            
            
        except Exception as e:
            raise CustomException(e,sys)