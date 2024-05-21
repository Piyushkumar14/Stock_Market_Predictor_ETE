import os
from src.stock_predictor import logger
from src.stock_predictor.entity.config_entity import DataTransformationConfig
from sklearn.model_selection import train_test_split
import pandas as pd


class DataTransformation:
    def __init__(self, config: DataTransformationConfig):
        self.config = config

    def transform_data(self):
        data = pd.read_csv(self.config.data_path, parse_dates=['Date'])

        data['Date'] = (data['Date'] - pd.Timestamp("1970-01-01")) // pd.Timedelta('1D')

        try:
            # Perform data transformation here
            del data["Dividends"]
            del data["Stock Splits"]

            data["Tomorrow"] = data["Close"].shift(-1)
            data["Target"] = (data["Tomorrow"] > data["Close"]).astype(int)
            data = data.loc["1990-01-01":].copy()
            data.dropna(inplace=True)
            data.to_csv(self.config.data_path, index=False)
        except Exception as e:
            logger.error(f"Error in data transformation: {e}")
            raise e

    def train_test_spliting(self):
        data = pd.read_csv(self.config.data_path)

        # Split the data into training and test sets. (0.75, 0.25) split.
        train, test = train_test_split(data)

        train.to_csv(os.path.join(self.config.root_dir, "train.csv"), index=False)
        test.to_csv(os.path.join(self.config.root_dir, "test.csv"), index=False)

        logger.info("Splitted data into training and test sets")
        logger.info(train.shape)
        logger.info(test.shape)

        print(train.shape)
        print(test.shape)
