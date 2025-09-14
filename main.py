from fastapi import FastAPI
import pandas as pd

app = FastAPI()

# Load datasets
farmers = pd.DataFrame({
    "farmer_id": [1, 2, 3],
    "name": ["Ram", "Sita", "Anil"],
    "location": ["VillageA", "VillageB", "VillageC"],
    "soil_type": ["loamy", "clay", "sandy"],
    "avg_rainfall_mm": [800, 400, 200],
    "budget_usd": [300, 150, 80]
})

market = pd.DataFrame({
    "crop": ["Wheat", "Rice", "Maize"],
    "price_usd": [200, 180, 150],
    "demand_index": [0.8, 0.9, 0.6]
})


@app.get("/")
def home():
    return {"message": "Sustainable Farming Advisor Backend is running"}

@app.get("/farmers")
def get_farmers():
    return farmers.to_dict(orient="records")

@app.get("/market")
def get_market():
    return market.to_dict(orient="records")

@app.get("/recommend/{farmer_id}")
def recommend_crop(farmer_id: int):
    farmer = farmers[farmers["farmer_id"] == farmer_id].iloc[0]
    
    # Simple recommendation logic
    if farmer["soil_type"] == "loamy":
        crop = "Wheat"
    elif farmer["soil_type"] == "clay":
        crop = "Rice"
    else:
        crop = "Maize"

    return {
        "farmer": farmer["name"],
        "recommended_crop": crop
    }
