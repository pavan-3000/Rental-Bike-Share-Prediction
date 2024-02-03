import joblib
from pathlib import Path
import numpy as np
import pandas as pd


class PredictionPipeline:
    def __init__(self):
        self.model = joblib.load(Path("artifacts/model_trainer/model.joblib_DecisionTree.joblib"))
        
        
        
    def predict(self,data):
        prediction = self.model.predict(data)
        
        return prediction