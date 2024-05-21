import os
from src.stock_predictor import logger
from src.stock_predictor.entity.config_entity import ModelTrainerConfig
from sklearn.ensemble import RandomForestRegressor
import joblib
import pandas as pd


class ModelTrainer:
    def __init__(self, config: ModelTrainerConfig):
        self.config = config

    def training(self):
        train_data = pd.read_csv(self.config.train_data_path)
        test_data = pd.read_csv(self.config.test_data_path)

        train_x = train_data.drop([self.config.target_column], axis=1)
        test_x = test_data.drop([self.config.target_column], axis=1)
        train_y = train_data[self.config.target_column]
        test_y = test_data[self.config.target_column]

        lr_model = RandomForestRegressor(max_depth=self.config.max_depth, min_samples_leaf=self.config.min_samples_leaf)
        lr_model.fit(train_x, train_y)

        joblib.dump(lr_model, os.path.join(self.config.root_dir, self.config.model_name))
