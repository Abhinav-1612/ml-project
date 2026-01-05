#here we do prediction of data afer taking users adata in post methid of web app
import sys # for exception handelingg
import pandas as pd
from src.exception import CustomException
from src.utils import load_object # to load pickle file

#predict pipeline
class PredictPipeline:
    def __init__(self):
        
        pass
    def predict(self,features):
        try:
             #taking path of both pkl files once data preprocessing and then predicting
             model_path='artifacts\model.pkl'
             preprocessor_path='artifacts\preprocessor.pkl'
             
             #this will load the pkl file ,declared in utils.py for loading the pkl file there only 
             model=load_object(file_path=model_path) 
             preprocessor=load_object(file_path=preprocessor_path) 
             
             #now predicting first scaling then predicting
             data_scaled=preprocessor.transform(features)
             preds=model.predict(data_scaled) 
             return preds
        except Exception as e:
            raise CustomException(e,sys)



class CustomData: #for taking data of web app in this declared variable only 
    def __init__(  self,
        gender: str,
        race_ethnicity: str,
        parental_level_of_education,
        lunch: str,
        test_preparation_course: str,
        reading_score: int,
        writing_score: int):
         
         # mapping of taked data
        self.gender = gender

        self.race_ethnicity = race_ethnicity

        self.parental_level_of_education = parental_level_of_education

        self.lunch = lunch

        self.test_preparation_course = test_preparation_course

        self.reading_score = reading_score

        self.writing_score = writing_score
        



#whatever we take input from web app will get mapped to this function values  and converted to dataframe as model is trainde as dataframe 
    def get_data_as_data_frame(self):
        try:
            custom_data_input_dict = {
                "gender": [self.gender],
                "race_ethnicity": [self.race_ethnicity],
                "parental_level_of_education": [self.parental_level_of_education],
                "lunch": [self.lunch],
                "test_preparation_course": [self.test_preparation_course],
                "reading_score": [self.reading_score],
                "writing_score": [self.writing_score],
            }

            return pd.DataFrame(custom_data_input_dict)# converted to df

        except Exception as e:
            raise CustomException(e, sys)

