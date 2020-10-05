from flask import request, render_template
from app import app
import requests

@app.route('/')
@app.route('/input')
def input_page():

	return render_template("input.html")

@app.route('/output')
def output_page():

	text  = request.args.get("text")
	data  = '{"text":"' + text + '"}'

	result = requests.post(url   = "https://modelapi-j3zdo3lhcq-uc.a.run.app/predict",
                         data    = data,
                         headers = {'Content-Type':'application/json'})

	topic  = result.json()["label"]

	return render_template("output.html", text=text, topic =topic)