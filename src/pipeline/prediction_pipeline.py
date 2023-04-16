import os
import sys
from src.config.configuration import *
from src.exception import GemstoneException
from src.logger import logging
from src.utils import load_model
import pandas as pd

class PredictPipeline:
    def __init__(self):
        pass
    
    def predict(self,features):
        try:
            preprocessor_path = preprocessing_obj_file
            model_path = model_file_path
            
            preprocessor = load_model(preprocessor_path)
            model = load_model(model_path)
            
            data_scaled = preprocessor.transform(features)
            
            pred = model.predict(data_scaled)
            return pred
        
        except Exception as e:
            logging.info("Error Occured in PredictPipeline")
            raise GemstoneException(e,sys)
        
class CustomData:
    def __init__(self,
                carat:float,
                cut:str,
                color:str,
                clarity:str,
                depth:float,
                table:float,
                x:float,
                y:float,
                z:float,):
        
        self.carat=carat
        self.cut = cut
        self.color = color
        self.clarity = clarity
        self.depth=depth
        self.table=table
        self.x=x
        self.y=y
        self.z=z
        
    def get_data_as_dataframe(self):
        try:
            custom_data_input_dict = {
                'carat':[self.carat],
                'cut':[self.cut],
                'color':[self.color],
                'clarity':[self.clarity],
                'depth':[self.depth],
                'table':[self.table],
                'x':[self.x],
                'y':[self.y],
                'z':[self.z]
            }
    
            df = pd.DataFrame(custom_data_input_dict)
            logging.info("DataFrame gathered")
            
            return df
        except Exception as e:
            logging.info("Error Occured in Custom Data")
            raise GemstoneException(e,sys)
        