import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression

CROP_DATA_FILE = "data/crop_data.csv"

def predict_crop_prices(crop, location):
    try:
        data = pd.read_csv(CROP_DATA_FILE)
        filtered_data = data[(data["Crop"] == crop) & (data["Location"] == location)]
        if filtered_data.empty:
            return []
        X = filtered_data[["Month", "Year"]]
        y = filtered_data["Price"]
        model = LinearRegression().fit(X, y)
        future_months = pd.DataFrame({"Month": np.arange(1, 7), "Year": [2025]*6})
        predictions = model.predict(future_months)
        return predictions
    except:
        return []
