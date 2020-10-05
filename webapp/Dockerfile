FROM python:3.7-alpine

# install dependencies first
RUN pip install flask==1.0.2 gunicorn==19.9.0 requests==2.23.0

# set up file system
RUN mkdir ds
WORKDIR /ds

# copy the files over
COPY webapp.py /ds
COPY app /ds/app

CMD exec gunicorn -w 2 -t 2 -b 0.0.0.0:8080 webapp:app
