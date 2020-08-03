from flask import Flask, request
import json
import joblib
import pandas as pd
import imblearn
from modelapi.Tokenizer import StemTokenizer
from modelapi.Relabeler import relabel

app = Flask(__name__)


@app.route('/predict', methods=['POST'])
def predict():
  if request.method == 'POST':
    try:
      text = request.json['text']
      df   = pd.DataFrame({"text":[text]})

      model = joblib.load("model/weighted_svm.joblib")
      result = model.predict(df)
      label  = relabel(result[0])
      
      return json.dumps(label)

    except:
      return json.dumps({'trace': traceback.format_exc()})


if __name__ == "__main__":
  app.run(host='0.0.0.0', port=8080)