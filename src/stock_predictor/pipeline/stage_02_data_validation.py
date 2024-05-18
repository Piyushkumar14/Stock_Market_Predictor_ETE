from src.stock_predictor.config.configuration import ConfigurationManager
from src.stock_predictor.components.data_validation import DataValidation
from src.stock_predictor import logger


STAGE_NAME = "Data Ingestion stage"


class DataValidationTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        data_ingestion_config = config.get_data_validation_config()
        data_ingestion = DataValidation(config=data_ingestion_config)
        data_ingestion.validate_all_columns()

if __name__ == '__main__':
    try:
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        obj = DataValidationTrainingPipeline()
        obj.main()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
    except Exception as e:
        logger.exception(e)
        raise e

