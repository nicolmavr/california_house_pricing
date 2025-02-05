from numpy import ndarray

def transformPrediction(prediction:ndarray):
    """
        Transforms the model output (ndarray size 1) to a float with 2 digit floating point precision
    """
    if (prediction.size!=1):
        raise ValueError("Predictions array size must be 1")
    toFloat = float(prediction[0])
    return round(toFloat,2)
    