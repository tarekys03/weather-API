import uvicorn
from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import pandas as pd
import os

from predictor import (
    classify_temperature,
    classify_humidity,
    classify_barometer,
    classify_windspeed,
    classify_Rain,
    classify_Light
)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all for testing; restrict in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def home():
    return {"message": "API Ready to receive data and analyze faults"}

@app.post("/predict/")
async def predict(file: UploadFile = File(...)):
    try:
        if not file.filename.endswith('.csv'):
            raise HTTPException(status_code=400, detail="Only CSV files are supported.")

        df = pd.read_csv(file.file)

        # Ensure required columns exist
        required_columns = ['Temperature', 'Humidity', 'Barometer', 'Windspeed', 'Rain', 'Light']
        for col in required_columns:
            if col not in df.columns:
                raise HTTPException(status_code=400, detail=f"Missing column: {col}")

        # Apply classification functions
        df['Temp_Fault'] = df['Temperature'].apply(classify_temperature)
        df['Humidity_Fault'] = df['Humidity'].apply(classify_humidity)
        df['Barometer_Fault'] = df['Barometer'].apply(classify_barometer)
        df['Wind_Fault'] = df['Windspeed'].apply(classify_windspeed)
        df['Rain_Fault'] = df['Rain'].apply(classify_Rain)
        df['Light_Fault'] = df['Light'].apply(classify_Light)

        # Save result to a new file (optional)
        output_path = "predicted_output.csv"
        df.to_csv(output_path, index=False)

        return {
            "message": "Predictions complete",
            "records": df.to_dict(orient="records")
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
