"""
##################################################################
#                                                                #
#                      MAIN REST API FILE                        #
#                                                                #
##################################################################

This file will be the main file of your REST API.
Use it to add an endpoint /predict that will be used to ask your model
for predictions.

You can use any technology you find suitable to develop your REST API, but make sure
to explain how to make it work.

launch with

 uvicorn app.main:app --reload
"""
from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
import pickle
import numpy as np
from fastapi.responses import HTMLResponse

# Load your model
with open('data/model_arima.pkl', 'rb') as model_file:
    model_arima = pickle.load(model_file)

app = FastAPI()

# Set up Jinja2 templates
templates = Jinja2Templates(directory="templates")

# Define the input data schema for prediction
class PredictionInput(BaseModel):
    steps: int

# Root endpoint - render the HTML with the button
@app.get("/", response_class=HTMLResponse)
def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

# Prediction endpoint
@app.post("/predict")
def predict(input: PredictionInput):
    try:
        # Use the loaded ARIMA model to make predictions
        forecast = model_arima.forecast(steps=input.steps)
        
        # Convert the forecasted values to a list for API response
        forecast_list = forecast.tolist()
        
        return {
            "forecast": forecast_list,
            "message": f"Forecast for {input.steps} steps ahead."
        }
    except Exception as e:
        return {"error": str(e), "message": "Error occurred during prediction."}