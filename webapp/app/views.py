from flask import request, render_template
from app import app
import requests
import re

@app.route('/')
@app.route('/input')
def input_page():

	return render_template("input.html")

@app.route('/output')
def output_page():

	raw_text  = request.args.get("text")
	text      = re.sub(r"[^a-zA-Z0-9_]", " ", raw_text)

	data  = '{"text":"' + text + '"}'

	result = requests.post(url   = "https://modelapi-j3zdo3lhcq-uc.a.run.app/predict",
                         data    = data,
                         headers = {'Content-Type':'application/json'})

	topic  = result.json()["label"]

	return render_template("output.html", text=text, topic =topic)