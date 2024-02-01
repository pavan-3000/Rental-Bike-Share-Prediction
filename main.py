from src.mlproject.logger import logging
from src.mlproject.exception import CustomException
import sys
from src.mlproject.pipeline.data_ingestion_pipeline import DataIngestionPipeline
from src.mlproject.pipeline.data_validation_pipeline import DataValidationPipeline
from src.mlproject.pipeline.data_transformation_pipeline import DataTransformationPipeline


try:
    logging.info(' data ingestion as stared')
    ingestion_obj = DataIngestionPipeline()
    ingestion_obj.main()
except Exception as e:
    raise CustomException(e,sys)



try:
    logging.info("data validation is stared ")
    validation_obj = DataValidationPipeline()
    validation_obj.main()
    
    logging.info("data validaiton has sucessfully completed")
    
except Exception as e:
    raise CustomException(e,sys)





try:
    logging.info("data transformation has stared ")
    
    trans_obj = DataTransformationPipeline()
    trans_obj.main()
    
    logging.info("data transfomation has completed sucessfully")
    
    
    
except Exception as e:
    raise CustomException(e,sys)