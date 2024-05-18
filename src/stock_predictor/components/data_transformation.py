import os
from src.stock_predictor import logger
from src.stock_predictor.entity.config_entity import DataTransformationConfig
from sklearn.model_selection import train_test_split
import pandas as pd


class DataValidation:
    def __init__(self, config: DataTransformationConfig):
        self.config = config

    def transform_data(self) -> pd.DataFrame:
        data = pd.read_csv(self.config.data_path)

        try:
            # Perform data transformation here
            del data["Dividends"]
            del data["Stock Splits"]

            data["Tomorrow"] = data["Close"].shift(-1)
            data["Target"] = (data["Tomorrow"] > data["Close"]).astype(int)
            return data
        except Exception as e:
            logger.error(f"Error in data transformation: {e}")
            raise e

    def train_test_splitting(self):
