from src.mlproject.logger import logging
from src.mlproject.exception import CustomException
import sys
from src.mlproject.entity.config_entity import ModelTrainerConfig
from src.mlproject.config.configuration import ConfigManager

from sklearn.ensemble import RandomForestRegressor
from xgboost import XGBRegressor
import pandas as pd
import joblib
import os


class ModelTrainer:
    def __init__(self,config:ModelTrainerConfig):
        self.config = config
        
        
    def get_model(self):
        try:
            train = pd.read_csv(self.config.train_data_path)
            test = pd.read_csv(self.config.test_data_path)
            
            x_train = train.drop(self.config.TARGET_NAME,axis=1)
            y_train = train[self.config.TARGET_NAME]
            
            
            x_test = test.drop(self.config.TARGET_NAME,axis=1)
            y_test = test[self.config.TARGET_NAME]
            
            model = XGBRegressor()
            
            model.fit(x_train,y_train)
            
            joblib.dump(model,os.path.join(self.config.root_dir,self.config.model_name))
            
            
        except Exception as e:
            raise CustomException(e,sys)
