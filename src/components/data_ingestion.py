from src.logging.logger import logging
from src.exception.custom_exception import CustomException
from src.entity.config_entity import DataIngestionConfig
from src.entity.artifact_entity import DataIngestionArtifact
import os,sys,kagglehub
import pandas as pd
from sklearn.model_selection import train_test_split
import time

class DataIngestion:
    def __init__(self,data_ingestion_config:DataIngestionConfig):
        self.data_ingestion_config=data_ingestion_config
       
    def importing_data_as_df(self):
        try:
            logging.info("importing data from kaggle is started")
            
            # Retry logic for timeout issues
            max_retries = 3
            for attempt in range(max_retries):
                try:
                    path = kagglehub.dataset_download("mlg-ulb/creditcardfraud")
                    print("Path to dataset files:", path)
                    dowloaded_path="C:\\Users\\Rishad R\\.cache\\kagglehub\\datasets\\mlg-ulb\\creditcardfraud\\versions\\3"
                    csv_filename="creditcard.csv"
                    csv_path=os.path.join(dowloaded_path,csv_filename)
                    df=pd.read_csv(csv_path)
                    return df
                except Exception as e:
                    if attempt < max_retries - 1:
                        logging.warning(f"Attempt {attempt + 1} failed, retrying in 10 seconds...")
                        time.sleep(10)
                    else:
                        raise e
                        
        except Exception as e:
            raise CustomException(e,sys)
       
    def export_data(self,df:pd.DataFrame):
        try:
            feature_store_filepath=self.data_ingestion_config.data_ingestion_featured_filepath
            dirname=os.path.dirname(feature_store_filepath)
            os.makedirs(dirname,exist_ok=True)
            df.to_csv(feature_store_filepath,index=False,header=True)
            return df
        except Exception as e:
            raise CustomException(e,sys)
       
    def train_test_split_ratio(self,df):
        try:
            ratio=self.data_ingestion_config.data_ingestion_train_test_split_ratio
            train_data,test_data=train_test_split(df,test_size=ratio)
            dir_path=os.path.dirname(self.data_ingestion_config.data_ingestion_train_filepath)
            os.makedirs(dir_path,exist_ok=True)
       
            train_data.to_csv(self.data_ingestion_config.data_ingestion_train_filepath,
                              index=False,header=True)
            test_data.to_csv(self.data_ingestion_config.data_ingestion_test_filepath,
                             index=False,header=True)
        except Exception as e:
            raise CustomException(e,sys)
       
    def initiate_data_ingestion(self):
        try:
            logging.info("data ingestion initiated")
            dataframe=self.importing_data_as_df()
            df=self.export_data(dataframe)
            self.train_test_split_ratio(df)  # Fixed method name
            logging.info("train test split is done")
            data_ingestion_artifact=DataIngestionArtifact(train_file_path=self.data_ingestion_config.data_ingestion_train_filepath,
                        test_file_path=self.data_ingestion_config.data_ingestion_test_filepath)
            logging.info("train file path and test file path are into the artifact")
            return data_ingestion_artifact
           
        except Exception as e:
            raise CustomException(e,sys)