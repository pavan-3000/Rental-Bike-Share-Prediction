from src.mlproject.logger import logging
from src.mlproject.exception import CustomException
import sys

from src.mlproject.entity.config_entity import ModelEvalutionConfig
from src.mlproject.config.configuration import ConfigManager

from src.mlproject.components.model_evalution import ModelEvalution


class ModelEvalutionPipeline:
    def __init__(self) -> None:
        pass 
    
    def main(self):
        try:
            logging.info("modell evalution pipelime as stared")
            eva_obj = ConfigManager()
            eva_obj = eva_obj.ModelEvalutionManager()
            model_eva = ModelEvalution(config=eva_obj)
            model_eva.save_score()
            
            logging.info("model evalution has created")
            
        except Exception as e:
            raise CustomException(e,sys)
