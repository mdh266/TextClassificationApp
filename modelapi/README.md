# Running Locally Without Docker
---------------
	cd app
	python main.py



# Building & Running Locally With Docker
---------------
Build the image:
	
	docker build -t modelapi .

Spin up container:

	docker run -ip 8080:8080 modelapi



# Deploying To Google Cloud Run
------------
Submit the image to Google Container Registry:

	gcloud builds submit --tag gcr.io/<project-id>/modelapi

Deploy the app to Cloud Run

	gcloud run deploy --image gcr.io/<project-id>/modelapi --platform managed