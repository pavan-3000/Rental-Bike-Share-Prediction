from pathlib import Path
from dataclasses import dataclass



@dataclass
class DataIngestionConfig:
    root_dir:Path
    source_URL: str
    local_data_file: Path
    unzip_path: Path

@dataclass
class DataValidationConfig:
    root_dir: Path
    data_path: Path
    STATUS_INFO: str
    all_schema: list
    
@dataclass
class DataTransformationConfig:
    root_dir: Path
    data_path: Path
    
    
@dataclass
class ModelTrainerConfig:
    root_dir: Path
    train_data_path: Path
    test_data_path: Path
    model_name: str
    TARGET_NAME: list
    
    
@dataclass
class ModelEvalutionConfig:
    root_dir: Path
    test_data_path: Path
    model_path: Path
    metric_file_name: str
    target_name: list