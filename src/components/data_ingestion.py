# contains code to read some data from any databse or from elsewhrere
# it play imp role when u working in team u reqire data collecting data from various sources 
import os 
import sys 
from src.exception import CustomException # for daeling exceptions 
from src.logger import logging 
import pandas as pd 
from sklearn.model_selection import train_test_split
from dataclasses import dataclass

@dataclass
#we defining this function so that we are giving input to datainegestion config and it saves our data -train test and data  in artifacts folder 
class DataIngestionConfig:
    train_data_path:str=os.path.join('artifacts',"train.csv")
    test_data_path:str=os.path.join('artifacts',"test.csv")
    raw_data_path:str=os.path.join('artifacts',"data.csv")

class DataIngestion: # when called this class uper values get saved in this below defined variable 
    def __init__(self):
        self.ingestion_config=DataIngestionConfig()

    def initiate_data_ingestion(self):
        logging.info("entered the data ingestion method or component ")
        try:
            df=pd.read_csv('notebook\data\stud.csv') # here u can read form sql or mongodb also 
            logging.info ('read the dataset as dataframe ')# updating the log file 

            #creating files of artifacts with train anda al datas 
          
            os .makedirs(os.path.dirname(self.ingestion_config.train_data_path),exist_ok=True)  #crating ofolder for train data 
            
            df.to_csv(self.ingestion_config.raw_data_path,index=False,header=True) # for raw data

            logging.info("train test split inittiated ")
            # splitting data and storing as train and test 
            train_set,test_set=train_test_split(df,test_size=0.2,random_state=42)
            
            train_set.to_csv(self.ingestion_config.train_data_path,index=False,header=True)

            test_set.to_csv(self.ingestion_config.test_data_path,index=False,header=True)
            logging.info("Ingestion of data is completed ")
            return (
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path
            ) # as we need this info for data transformation which is next step 
        except Exception as e:
            raise   CustomException(e,sys)   

if __name__=="__main__":
    obj=DataIngestion()
    obj.initiate_data_ingestion()
