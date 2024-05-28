from mlproject import logger
from mlproject.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from mlproject.pipeline.stage_02_data_validation import DataValidationTrainingPipeline
from mlproject.pipeline.stage_03_data_transformation import DataTransformationTrainingPipeline
from mlproject.pipeline.stage_04_model_trainer import ModelTrainerTrainingPipeline
from mlproject.pipeline.stage_05_model_evaluation import ModelEvaluationTrainingPipeline

def main():
   STAGE_NAME = "Data Ingestion stage"
   try:
      logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<") 
      data_ingestion = DataIngestionTrainingPipeline()
      data_ingestion.main()
      logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
   except Exception as e:
         logger.exception(e)
         raise e

   STAGE_NAME = "Data Validation stage"
   try:
      logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<") 
      data_ingestion = DataValidationTrainingPipeline()
      data_ingestion.main()
      logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
   except Exception as e:
         logger.exception(e)
         raise e



   STAGE_NAME = "Data Transformation stage"
   try:
      logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<") 
      data_ingestion = DataTransformationTrainingPipeline()
      data_ingestion.main()
      logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
   except Exception as e:
         logger.exception(e)
         raise e

   STAGE_NAME = "Model Trainer stage"
   try:
      logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<") 
      data_ingestion = ModelTrainerTrainingPipeline()
      data_ingestion.main()
      logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
   except Exception as e:
         logger.exception(e)
         raise e


   STAGE_NAME = "Model evaluation stage"
   try:
      logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<") 
      data_ingestion = ModelEvaluationTrainingPipeline()
      data_ingestion.main()
      logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
   except Exception as e:
         logger.exception(e)
         raise e


if __name__ == '__main__':
    main()