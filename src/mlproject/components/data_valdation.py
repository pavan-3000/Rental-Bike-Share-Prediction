from src.mlproject.logger import logging
from src.mlproject.exception import CustomException
import sys

from src.mlproject.entity.config_entity import DataValidationConfig
from src.mlproject.config.configuration import ConfigManager
import pandas as pd
class DataValidation:
    def __init__(self,config:DataValidationConfig):
        self.config = config
        
    def validate_all_col(self):
        try:
            
            Validation_status = None
            df = pd.read_csv(self.config.data_path)
            all_col = list(df.columns)
            valid_col = self.config.all_schema.keys()
            
            for col in all_col:
                if col not in valid_col:
                    Validation_status = False
                    with open(self.config.STATUS_INFO,'w') as f:
                        f.write(f"validation status: {Validation_status}")
                        
                else:
                    Validation_status = True
                    with open(self.config.STATUS_INFO,'w') as f:
                        
                        f.write(f"validation status: {Validation_status}")
                    
            return Validation_status
        
        
            logging,info('Validation info is added')
 
            
            
            
            
        except Exception as e:
            raise CustomException(e,sys)