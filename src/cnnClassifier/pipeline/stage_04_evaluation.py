from cnnClassifier.components.evaluation import Evaluation
from cnnClassifier.config.configuration import ConfigurationManager
from cnnClassifier import logger

STAGE_NAME = 'Evaluation stage'

class EvaluationPipeline:
    def __init__(self) -> None:
        pass

    def main(self):
        config = ConfigurationManager()
        val_config = config.get_validation_config()
        evaluation = Evaluation(val_config)
        evaluation.evaluation()
        evaluation.save_score()


if __name__ == "main":
    try:
        logger.info(f"*********************")
        logger.info(f">>>>>>>>>>>> {STAGE_NAME} started <<<<<<<<<")
        obj = EvaluationPipeline()
        obj.main()
        logger.info(f">>>>>>>>>>>> {STAGE_NAME} completed <<<<<<<<< \n\n x======================x")
    except Exception as e:
        logger.exception(e)
        raise e