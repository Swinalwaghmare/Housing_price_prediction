import os
import sys

import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression, Ridge, Lasso, ElasticNet
from src.config.configuration import *
from src.exception import GemstoneException
from src.logger import logging

from src.utils import *

from dataclasses import dataclass

@dataclass
class ModelTrainerConfig:
    trained_model_file_path = model_file_path
    
class ModelTrainer:
    def __init__(self):
        self.model_trainer_config = ModelTrainerConfig()
        
    def intiate_model_training(self,train_array,test_array):
        try:
            logging.info("="*50)
            logging.info("Model Training Intiated")
            logging.info("="*50)
            
            X_train, y_train , X_test, y_test = (train_array[:,:-1],
                                                 train_array[:,-1],
                                                 test_array[:,:-1],
                                                 test_array[:,-1]
                                                 )
            
            models = {
                'LinearRegression':LinearRegression(),
                'Ridge':Ridge(),
                'Lasso':Lasso(),
                'Ridge':Ridge(),
                'ElasticNet':ElasticNet()
            }
            
            model_report:dict = evaluate_model(X_train,y_train,X_test,y_test,models)
            print(model_report)
            print(f'\n{"="*50}')
            logging.info(f'Model Report: {model_report}')
            
            best_model_score = max(sorted(model_report.values()))
            
            best_model_name = list(model_report.keys())[
                list(model_report.values()).index(best_model_score)]
            
            best_model = models[best_model_name]
            
            print(f'Best Model Found, Model Name: {best_model_name}, R2 Score: {best_model_score}')
            
            logging.info("="*50)
            logging.info(f'Best Model Found, Model Name: {best_model_name}, R2 Score: {best_model_score}')

            save_object(
                file_path=self.model_trainer_config.trained_model_file_path,
                obj=best_model
            )
            
        except Exception as e:
            logging.info("Exception occured at Model Trainer")
            raise GemstoneException(e,sys)

