# Running Locally Without Docker
---------------
	cd app
	python main.py

Then go to http://localhost:8080

# Building & Running Locally With Docker
---------------
Build the image:
	
	docker build -t webapp .

Spin up container:

	docker run -ip 8080:8080 webapp

Then go to http://localhost:8080

# Deploying to Google Cloud Run
------------
Submit the image to Google Container Registry:

	gcloud builds submit --tag gcr.io/<project-id>/docwebapp

Deploy the app to Cloud Run

	gcloud run deploy --image gcr.io/<project-id>/docwebapp --platform managed