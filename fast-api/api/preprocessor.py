from .models import PredictionRequest, OceanProximity
from sklearn.preprocessing import LabelEncoder


import pandas as pd



class Preprocessor:
    def __init__(self,labelEncoder:LabelEncoder):
        self._labelEncoder = labelEncoder

    def _fitTransform(self,proximity: OceanProximity):
        return self._labelEncoder.transform([proximity.value])[0]
    
    def encode(self,prediction_request:PredictionRequest):
        """
            Encodes the request to DataFrame and transorfms the necessary data
        """
        return pd.DataFrame([{
            "longitude":prediction_request.longitude,
            "housing_median_age":prediction_request.housing_median_age,
            "households":prediction_request.households,
            "median_income":prediction_request.median_income,
            "ocean_proximity":self._fitTransform(prediction_request.ocean_proximity),
            "rooms_per_household":(prediction_request.total_rooms/prediction_request.households),
            "bedrooms_per_household":(prediction_request.total_bedrooms/prediction_request.households),
            "population_per_household":(prediction_request.total_rooms/prediction_request.households),
        }])