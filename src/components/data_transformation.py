#code related to any transformation of data  like encoding and scaling , handling pickle file and saving it
# already done in ipynb but for professional doing this 
import sys
from dataclasses import  dataclass

import numpy as np
import pandas as pd
from sklearn.compose import ColumnTransformer #see ipynb what we used
from sklearn.impute import SimpleImputer #for missing values
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder,StandardScaler

# as to do exception handling and logging 
from src.exception import CustomException
from src.logger import logging
import os

from src.utils import save_object

@dataclass # it is a decorator which automaticcaly asssigns all like __init__ and all and maintains class perfectly 
class DataTransformationConfig:
    preprocessor_obj_file_path=os.path.join('artifacts',"preprocessor.pkl") # all the models get saved as pkl here

class DataTransformation:
    def __init__(self):
        self.data_transformation_config=DataTransformationConfig()

    def get_data_transformer_object(self):
        '''
         this function responsible for data transformation
        '''
        try:
            numerical_columns =["reading_score", "writing_score"]
            categorical_columns =[
                "gender", 
                "race_ethnicity",
                "parental_level_of_education", 
                "lunch",
                "test_preparation_course",
                 ]
            num_pipeline=Pipeline(
                steps=[
                    ("imputer",SimpleImputer(strategy="median")),
                    ("scaler",StandardScaler())

                ]
            )
            cat_pipeline=Pipeline(
                steps=[
                ("imputer",SimpleImputer(strategy="most_frequent")),# replacing missing values with mode 
                ("one_hot_encoder",OneHotEncoder()),
                ("scaler",StandardScaler(with_mean=False))
                ]
            )
            logging.info(f"caategorical columns:{categorical_columns}")
            logging.info(f"numerical columns:{numerical_columns}")

            #column transformer
            preprocessor=ColumnTransformer(
                [
                    ("num_pipeline",num_pipeline,numerical_columns),
                    ("cat_pipeline",cat_pipeline,categorical_columns)
                ]
            )

            return preprocessor

        except Exception as e:
            raise CustomException(e,sys)

    def initiate_data_transformation(self,train_path,test_path):

        try:
            train_df=pd.read_csv(train_path)
            test_df=pd.read_csv(test_path)
            logging.info("read the train and test data completed ")  
            logging.info ("obtaining preprocessing object ")
            preprocessing_obj=self.get_data_transformer_object()# calling this function for transformation of data
            target_column_name="math_score"
            numerical_columns =["reading_score", "writing_score"]
            
            input_feature_train_df=train_df.drop(columns=[target_column_name],axis=1)
            target_feature_train_df=train_df[target_column_name]

            input_feature_test_df=test_df.drop(columns=[target_column_name],axis=1)
            target_feature_test_df=test_df[target_column_name]
            
            logging.info(
                f"applying the preprocessing object on training dataframe and testing dataframe ."
            )
            input_feature_train_arr=preprocessing_obj.fit_transform(input_feature_train_df)
            input_feature_test_arr=preprocessing_obj.transform(input_feature_test_df)

       # what is role of np.c_ here 
            train_arr=np.c_[
                input_feature_train_arr,np.array(target_feature_train_df)

            ]
            test_arr=np.c_[
                input_feature_test_arr,np.array(target_feature_test_df) # we are combining bboth using np.c

            ]
            logging.info (f"saved preprocessing object ")

         #saving pickle file in hard drive ,we created this function in utils also 
            save_object(
                file_path=self.data_transformation_config.preprocessor_obj_file_path,
                obj=preprocessing_obj
            )

            return (
                train_arr,
                test_arr,
                self.data_transformation_config.preprocessor_obj_file_path,

            )
        except Exception as e:
            raise CustomException(e,sys)

