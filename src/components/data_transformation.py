from src.logging.logger import logging
from src.exception.custom_exception import CustomException
import os,sys
import pandas as pd
from src.entity.config_entity import DataTransformationConfig
from src.entity.artifact_entity import DataTransformationArtifact
from src.entity.artifact_entity import DataIngestionArtifact
from imblearn.over_sampling import SMOTE
import numpy as np
from src.utility.main_utility import save_numpy


class DataTransformation:
    def __init__(self,data_transformation_config:DataTransformationConfig,
                 data_ingestion_artifact:DataIngestionArtifact):
        self.data_transformation_config=data_transformation_config
        self.data_ingestion_artifact=data_ingestion_artifact
        
        
    @staticmethod
    def read_data(filepath:str)->pd.DataFrame:
        try:
            return pd.read_csv(filepath)
        except Exception as e:
            raise CustomException(e,sys)
        
        
        
    def initiate_data_transformation(self):
        try:
            train_df=DataTransformation.read_data(self.data_ingestion_artifact.train_file_path)
            test_df=DataTransformation.read_data(self.data_ingestion_artifact.test_file_path)
            
            x_train=train_df.drop('Class',axis=1)
            y_train=train_df['Class']
            
            x_test=test_df.drop('Class',axis=1)
            y_test=test_df['Class']
            
            smote=SMOTE(random_state=42)
            x_train_oversampled,y_train_oversampled=smote.fit_resample(x_train,y_train)
            
            train_arr=np.c_[x_train_oversampled,y_train_oversampled]
            x_test=x_test.to_numpy()
            y_test=y_test.to_numpy()
            
            test_arr=np.c_[x_test,y_test]
            
            save_numpy(self.data_transformation_config.data_transformation_train_filepath,train_arr)
            save_numpy(self.data_transformation_config.data_transformation_test_filepath,test_arr)
            
            data_transformation_artifact=DataTransformationArtifact(train_file_path=self.data_transformation_config.data_transformation_train_filepath,
                            test_file_path=self.data_transformation_config.data_transformation_test_filepath)
            
            return data_transformation_artifact
        except Exception as e:
            raise CustomException(e,sys)
    
        
        
        
        
        
        
        
        
        