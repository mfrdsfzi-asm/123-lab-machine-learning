from fastapi import FastAPI
import joblib
import uvicorn
from pydantic import BaseModel

import re
from nltk.stem import WordNetLemmatizer, PorterStemmer


app = FastAPI()
lemmatizer = WordNetLemmatizer()
stemmer = PorterStemmer()


class PredictionRequest(BaseModel):
    # Setting up the API schema.
    # Make sure to match the input feature with the model's expected input.
    text: str


def preprocess_text(text):
    # lowercase
    text = text.lower()

    # remove punctuation and special characters
    text = re.sub(r'[^a-zA-Z\s]', ' ', text)

    # remove digits
    text = re.sub(r'\d+', ' ', text)

    # lemmatization
    text = " ".join(
        [lemmatizer.lemmatize(word, pos='v')
         for word in text.split()]
        )

    # stemming
    text = " ".join([stemmer.stem(word) for word in text.split()])

    # remove extra spaces
    text = re.sub(r'\s+', ' ', text).strip()

    return text


# Endpoint to handle prediction requests
@app.post("/predict")
def predict(request: PredictionRequest):

    # Load the pre-trained model
    model_path = "../model_cls.pkl"
    model = joblib.load(model_path)

    # Make a prediction using the model
    preprocessed_text = preprocess_text(request.text)
    predicted_class = model.predict([preprocessed_text])

    # Return the prediction result
    return {"predicted_class": predicted_class[0]}


# Endpoint to handle prediction requests
@app.post("/estimate")
def estimate(request: PredictionRequest):

    # Load the pre-trained model
    model_path = "../model_estimate.pkl"
    model = joblib.load(model_path)

    # Make a prediction using the model
    preprocessed_text = preprocess_text(request.text)
    predicted_estimate = model.predict([preprocessed_text])

    # Return the prediction result
    return {"estimate": round(predicted_estimate[0], 2)}


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8003, reload=True)
