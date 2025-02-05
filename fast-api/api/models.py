from pydantic import BaseModel, Field
from enum import Enum

class OceanProximity(str, Enum):
    NEAR_BAY = "NEAR BAY"
    INLAND = "INLAND"
    NEAR_OCEAN = "NEAR OCEAN"
    ISLAND = "ISLAND"
    LESS_THAN_ONE_HOUR_OCEAN = "<1H OCEAN"

class PredictionRequest(BaseModel):
    longitude: float = Field(gt=-124.4820, le=-114.1315,example=-122.23)
    latitude: float = Field(ge=32.5288, le=42.0095,example=39.88)
    housing_median_age: float = Field(ge=0,example=41.0)
    total_rooms: float = Field(ge=0,example=880.0)
    total_bedrooms: float = Field(ge=0,example=129.0)
    population: float = Field(ge=0,example=322.0)
    households: float = Field(ge=0,example=126.0)
    median_income: float = Field(ge=0,example=8.3252)
    ocean_proximity: OceanProximity = Field(...,example="NEAR BAY")

class PredictionResponse(BaseModel):
    prediction: float = Field(ge=0,example=360006.44)