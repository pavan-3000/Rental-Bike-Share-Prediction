from src.mlproject.logger import logging
from src.mlproject.exception import CustomException
import sys

from src.mlproject.entity.config_entity import ModelTrainerConfig
from src.mlproject.config.configuration import ConfigManager
from src.mlproject.components.model_trainer import ModelTrainer




class ModelTrainerPipeline:
    def __init__(self):
        pass 
    
    
    def main(self):
        try:
            
            logging.info("data pipleine createing ")
            
            model_config = ConfigManager()
            model_config = model_config.ModelTrainerManager()
            model_trainer = ModelTrainer(config=model_config)
            model_trainer.get_model()
            
            logging.info("model pipeline has created")
            
            
        except Exception as e:
            raise CustomException(e,sys)