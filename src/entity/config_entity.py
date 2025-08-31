import os,sys
from datetime import datetime
from src import constant


class TrainingPipelineConfig:
    def __init__(self,timestamp=datetime.now()):
        timestamp=timestamp.strftime("%m_%d_%Y_%H_%M_%S")
        self.pipeline_name=constant.PIPELINE_NAME
        self.artifacts_name=constant.ARTIFACT_DIR
        self.artifacts_dir=os.path.join(self.artifacts_name,timestamp)
        self.timestamp:str=timestamp
        
class DataIngestionConfig:
    def __init__(self,train_pipeline_config:TrainingPipelineConfig):
        self.data_ingestion_dir:str=os.path.join(train_pipeline_config.artifacts_dir,
                    constant.DATA_INGESTION_DIR)
        self.data_ingestion_featured_filepath:str=os.path.join(self.data_ingestion_dir,
                    constant.DATA_INGESTION_FEATURE_DIR,
                    constant.DATA_INGESTION_RAW_FILENAME)
        self.data_ingestion_train_filepath:str=os.path.join(self.data_ingestion_dir,
                    constant.DATA_INGESTION_INGESTED_DIR,
                    constant.DATA_INGESTION_TRAIN_FILENAME)
        self.data_ingestion_test_filepath:str=os.path.join(self.data_ingestion_dir,
                    constant.DATA_INGESTION_INGESTED_DIR,
                    constant.DATA_INGESTION_TEST_FILENAME)
        self.data_ingestion_train_test_split_ratio:float=constant.TRAIN_TEST_SPLIT_RATIO