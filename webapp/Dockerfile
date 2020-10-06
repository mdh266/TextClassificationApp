FROM python:3.7-alpine

# copy the files over
COPY ./app app
COPY requirements.txt app
WORKDIR app

RUN pip install -r requirements.txt

CMD ["uvicorn","main:app", "--host","0.0.0.0", "--port", "8080"]

