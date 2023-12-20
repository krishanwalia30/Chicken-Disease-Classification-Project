from cnnClassifier import logger
from cnnClassifier.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from cnnClassifier.pipeline.stage_02_prepare_base_model import PrepareBaseModelTrainingPipeline
from cnnClassifier.pipeline.stage_03_training import ModelTrainingPipeline
from cnnClassifier.pipeline.stage_04_evaluation import EvaluationPipeline


# This is the entry point in the pipeline and comprises data ingestion stage
STAGE_NAME = "Data Ingestion stage"
try:
    logger.info(f">>>>>>>> stage {STAGE_NAME} started <<<<<<<<")
    obj = DataIngestionTrainingPipeline()
    obj.main()
    logger.info(f">>>>>>>>> stage {STAGE_NAME} completed <<<<<<<<<<< \n \n x==============x")
except Exception as e:
    logger.exception(e)
    raise e

# This is the second part of preparing the base model after ingesting the data
STAGE_NAME = "Prepare Base Model"
try:
    logger.info(f">>>>>>>> stage {STAGE_NAME} started <<<<<<<<")
    obj = PrepareBaseModelTrainingPipeline()
    obj.main()
    logger.info(f">>>>>>>>> stage {STAGE_NAME} completed <<<<<<<<<<< \n \n x==============x")
except Exception as e:
    logger.exception(e)
    raise e

# This is the training of the model created.
STAGE_NAME = "Training"
try:
    logger.info(f"********************")
    logger.info(f">>>>> stage {STAGE_NAME} started <<<<<<<")
    obj = ModelTrainingPipeline()
    obj.main()
    logger.info(f">>>>>>>>> stage {STAGE_NAME} completed <<<<<<< \n\n x==============x")
except Exception as e:
    logger.exception(e)
    raise e

# This is for evaluating our model 
STAGE_NAME = "Evaluation stage"
try:
    logger.info(f"*********************")
    logger.info(f">>>>>>>>>>>> {STAGE_NAME} started <<<<<<<<<")
    obj = EvaluationPipeline()
    obj.main()
    logger.info(f">>>>>>>>>>>> {STAGE_NAME} completed <<<<<<<<< \n\n x======================x")
except Exception as e:
    logger.exception(e)
    raise e