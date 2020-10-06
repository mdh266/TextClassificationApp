from modelapi.Tokenizer import StemTokenizer
from modelapi.Relabeler import relabel
import joblib

from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn
import imblearn

app = FastAPI()

class InputDoc(BaseModel):
  text  : str

class LabeledDoc(InputDoc):
  label : str

@app.get("/")
def root():
    return {"message": "Hello World"}

@app.post('/predict', response_model=LabeledDoc, status_code=200)
def predict(doc : InputDoc):
    """
    Help from https://testdriven.io/blog/fastapi-machine-learning/
    """

    text   = doc.text
    model  = joblib.load("models/weighted_svm.joblib")
    result = model.predict([text])
    label  = relabel(result[0])

    return {"text": text, "label":label}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
