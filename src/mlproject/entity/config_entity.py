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