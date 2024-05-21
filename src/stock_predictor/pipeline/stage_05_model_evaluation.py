from src.stock_predictor.config.configuration import ConfigurationManager
from src.stock_predictor.components.model_evaluation import ModelEvaluation
from src.stock_predictor import logger
from pathlib import Path

STAGE_NAME   = "Model Training stage"


class ModelEvaluatingPipeline:
    def __init__(self):
        pass;

    def main(self):
        config = ConfigurationManager()
        model_training_config = config.get_model_evaluation_config()
        model_training = ModelEvaluation(config=model_training_config)
        model_training.log_into_mlflow()


if __name__ == '__main__':
    try:
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        obj = ModelEvaluatingPipeline()
        obj.main()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<< \n\nx=================x")
    except Exception as e:
        logger.exception(e)
        raise e
