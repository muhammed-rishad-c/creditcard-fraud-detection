from src.entity.config_entity import TrainingPipelineConfig
from src.entity.config_entity import  DataIngestionConfig
from src.entity.artifact_entity import DataIngestionArtifact

from src.components.data_ingestion import DataIngestion


if __name__=="__main__":
    training_pipeline=TrainingPipelineConfig()
    data_ingestion_config=DataIngestionConfig(training_pipeline)
    data_ingestion=DataIngestion(data_ingestion_config)
    data_ingestion_artifact=data_ingestion.initiate_data_ingestion()
    
    
    