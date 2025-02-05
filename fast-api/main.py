from fastapi import Body,FastAPI,Query
import joblib
import pandas as pd
from typing import Annotated
from api.models import PredictionRequest, PredictionResponse
from api.preprocessor import Preprocessor
from api.postprocessor import transformPrediction

app = FastAPI()

## Load models
linear_regression_standard_model = joblib.load('models/linear_regression_standard_model.pkl')
random_forest_model = joblib.load('models/random_forest_model.pkl')
xgboost_model = joblib.load('models/xgboost_model.pkl')
labelEncoder = joblib.load('models/label_encoder.pkl')

preprocessor = Preprocessor(labelEncoder)


@app.post("/xgboost",response_model=PredictionResponse)
async def prediction_xgboost(prediction_request: Annotated[PredictionRequest, Body(embed=False)]):
    """
        Endpoint for XGBoost model
    """
    encoded_request=preprocessor.encode(prediction_request)
    prediction = xgboost_model.predict(encoded_request)
    result = transformPrediction(prediction)
    return PredictionResponse(prediction=result)


@app.post("/linear_regression",response_model=PredictionResponse)
async def prediction_linear_regression(prediction_request: Annotated[PredictionRequest, Body(embed=False)]):
    """
        Endpoint for linear regression model
    """
    encoded_request=preprocessor.encode(prediction_request)   
    prediction = linear_regression_standard_model.predict(encoded_request)
    result = transformPrediction(prediction)
    return PredictionResponse(prediction=result)


@app.post("/random_forest",response_model=PredictionResponse)
async def prediction_random_forest(prediction_request: Annotated[PredictionRequest, Body(embed=False)]):
    """
        Endpoint for random forest model
    """
    encoded_request=preprocessor.encode(prediction_request)
    prediction = random_forest_model.predict(encoded_request)
    result = transformPrediction(prediction)
    return PredictionResponse(prediction=result)