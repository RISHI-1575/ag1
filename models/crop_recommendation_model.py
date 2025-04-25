import pandas as pd

CROP_DATA_FILE = "data/crop_data.csv"

def recommend_crops(location, soil_type, land_size):
    try:
        # Load crop data
        data = pd.read_csv(CROP_DATA_FILE)
        
        # Filter data by location
        filtered_data = data[data["Location"] == location]
        
        # Example logic using historical price data
        crops_profit_demand = filtered_data.groupby("Crop").agg({
            "Price": "mean",
            "Demand": "mean"
        }).reset_index()
        
        # Sort by highest profit and demand
        crops_profit_demand["Profit_Level"] = crops_profit_demand["Price"] * land_size
        crops_profit_demand["Demand_Level"] = crops_profit_demand["Demand"]
        recommended_crops = crops_profit_demand.sort_values(
            by=["Profit_Level", "Demand_Level"], ascending=False
        ).head(5)
        
        return recommended_crops[["Crop", "Profit_Level", "Demand_Level"]]
    except Exception as e:
        print(f"Error in recommendation: {e}")
        return pd.DataFrame(columns=["Crop", "Profit_Level", "Demand_Level"])