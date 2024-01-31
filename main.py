from src.mlproject.logger import logging
from src.mlproject.exception import CustomException
import sys

from src.mlproject.pipeline.data_ingestion_pipeline import DataIngestionPipeline


try:
    logging.info(' data ingestion as stared')
    ingestion_obj = DataIngestionPipeline()
    ingestion_obj.main()
except Exception as e:
    raise CustomException(e,sys)