
import os

import pandas as pd
import joblib


class CustomData:
    '''
    Responsible for the mapping of html input data to the backend, it goes in the POST method
    '''
    def __init__(self,
                quantity: float,
                temperature: float,
                category: str,
                unit_price: float,
                day_of_month: int,
                hour: int):
        
        self.quantity = quantity
        self.temperature = temperature
        self.category = category
        self.unit_price = unit_price
        self.day_of_month = day_of_month
        self.hour = hour


    def get_data_as_DataFrame(self):
            
        custom_data_input_dict = {
            "quantity" : [self.quantity],
            "temperature": [self.temperature],
            "category": [self.category],
            "unit_price": [self.unit_price],
            "day_of_month": [self.day_of_month],
            "hour": [self.hour],
            }
        
        return pd.DataFrame(custom_data_input_dict)


class PredictPipeline:
    
    def __init__(self):
        self.model_path = os.path.join("final_model.pkl")
        self.transformation_path = os.path.join('transform_pipeline.pkl')

    def predict(self,features):
            
        model = joblib.load(self.model_path)
        transform_pipeline = joblib.load(self.transformation_path)

        column_names = list(transform_pipeline.named_steps['preprocessor'].named_transformers_['ohe'].get_feature_names_out()) +list(transform_pipeline.named_steps['preprocessor'].named_transformers_['standard_scaler'].get_feature_names_out())

        data_transformed = pd.DataFrame(transform_pipeline.transform(features).toarray(),columns=column_names)

        preds = model.predict(data_transformed)

        return preds