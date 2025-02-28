import os
import joblib
import pandas as pd
from xgboost import XGBClassifier
from xgboost import XGBRegressor
# currently the container not importing sklearn and column transformer
from sklearn.compose import ColumnTransformer, make_column_transformer
from sklearn.pipeline import Pipeline, make_pipeline
from sklearn.preprocessing import StandardScaler, MinMaxScaler, RobustScaler
from sklearn import preprocessing

def load_model(model_dir: str) -> Pipeline:
    """
    Load the model from the specified directory.
    """
    # Load the entire pipeline (which includes the ColumnTransformer and XGBClassifier)
    return joblib.load(os.path.join(model_dir, "xgboost_model.joblib"))

def predict(body: dict, model: Pipeline) -> dict:
    """
    Generate predictions for the incoming request using the model.
    """
    # Convert the incoming JSON data to a DataFrame
    features = pd.DataFrame.from_records(body["features"])
    
    # Make predictions using the pipeline
    predictions = model.predict(features).tolist()
    
    # Return predictions as a dictionary
    return {"predictions": predictions}


'''
def load_model(model_dir: str) -> XGBClassifier:
    """
    Load the model from the specified directory.
    """
    return joblib.load(os.path.join(model_dir, "xgboost_model.joblib"))


def predict(body: dict, model: XGBClassifier) -> dict:
    """
    Generate predictions for the incoming request using the model.
    """
    features = pd.DataFrame.from_records(body["features"])
    predictions = model.predict(features).tolist()
    return {"predictions": predictions}
'''