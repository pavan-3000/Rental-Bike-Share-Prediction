from src.mlproject.logger import logging
from src.mlproject.exception import CustomException
import sys

from src.mlproject.entity.config_entity import ModelEvalutionConfig
from src.mlproject.components.model_evalution import ModelEvalutionConfig
from src.mlproject.config.configuration import ConfigManager
import pandas as pd
import joblib
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
from src.mlproject.utils.common import save_json
from pathlib import Path
class ModelEvalution:
    def __init__(self,config:ModelEvalutionConfig):
        self.config  = config
        
    def evalute_metric(self,real_value,predict_value):
        
        mse = mean_squared_error(real_value,predict_value)
        mae = mean_absolute_error(real_value,predict_value)
        r2 = r2_score(real_value,predict_value)
        return mse,mae,r2
    
    def save_score(self):
        try:
            test = pd.read_csv(self.config.test_data_path)
            model = joblib.load(self.config.model_path)
            
            
            x_test = test.drop(self.config.target_name,axis=1)
            y_test = test[self.config.target_name]
            
            prediction = model.predict(x_test)
            
            (mse,mae,r2) = self.evalute_metric(y_test,prediction)
            
            score = {"mse": mse,"mae": mae , "r2":r2}
            save_json(path=Path(self.config.metric_file_name),data = score)
            
            
        except Exception as e:
            raise CustomException(e,sys)