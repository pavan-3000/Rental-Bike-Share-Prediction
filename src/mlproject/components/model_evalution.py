from src.mlproject.logger import logging
from src.mlproject.exception import CustomException
import sys

from src.mlproject.entity.config_entity import ModelEvalutionConfig
from src.mlproject.config.configuration import ConfigManager
import pandas as pd
import joblib
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
from src.mlproject.utils.common import save_json
from pathlib import Path

class ModelEvalution:
    def __init__(self, config: ModelEvalutionConfig):
        self.config = config

    def evaluate_metric(self, real_values, predicted_values):
        mse = mean_squared_error(real_values, predicted_values)
        mae = mean_absolute_error(real_values, predicted_values)
        r2 = r2_score(real_values, predicted_values)
        return mse, mae, r2

    def save_score(self):
        try:
            test = pd.read_csv(self.config.test_data_path)
            models = joblib.load(self.config.model_path)

            x_test = test.drop(self.config.target_name, axis=1)
            y_test = test[self.config.target_name]

            for name, model in models:
                predictions = model.predict(x_test)

                # Evaluate metrics
                (mse, mae, r2) = self.evaluate_metric(y_test, predictions)

                # Save scores with model name
                score = {"model_name": name, "mse": mse, "mae": mae, "r2": r2}
                save_json(path=Path(f"{self.config.metric_file_name}_{name}.json"), data=score)

        except Exception as e:
            raise CustomException(e, sys)
