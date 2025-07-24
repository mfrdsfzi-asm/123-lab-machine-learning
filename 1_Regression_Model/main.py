from fastapi import FastAPI
import joblib
import uvicorn
from pydantic import BaseModel

app = FastAPI()


class PredictionRequest(BaseModel):
    # Setting up the API schema.
    # Make sure to match the input feature with the model's expected input.
    weight: float


# Endpoint to handle prediction requests
@app.post("/predict")
def predict(request: PredictionRequest):

    # Load the pre-trained model
    model_path = "../model_lr.pkl"
    model = joblib.load(model_path)

    # Make a prediction using the model
    predicted_mpg = model.predict([[request.weight]])

    # Return the prediction result
    return {"predicted_mpg": predicted_mpg[0]}


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8003, reload=True)
