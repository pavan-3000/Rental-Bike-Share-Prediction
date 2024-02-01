from src.mlproject.logger import logging
from src.mlproject.exception import CustomException
import sys
from src.mlproject.pipeline.data_ingestion_pipeline import DataIngestion
from src.mlproject.pipeline.data_validation_pipeline import DataValidationPipeline

'''
try:
    logging.info(' data ingestion as stared')
    ingestion_obj = DataIngestionPipeline()
    ingestion_obj.main()
except Exception as e:
    raise CustomException(e,sys)
'''


try:
    logging.info("data validation is stared ")
    validation_obj = DataValidationPipeline()
    validation_obj.main()
    
    logging.info("data validaiton has sucessfully completed")
    
except Exception as e:
    raise CustomException(e,sys)