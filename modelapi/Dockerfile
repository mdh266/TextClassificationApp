FROM continuumio/miniconda3:4.8.2

# set up file system
RUN mkdir ds
RUN mkdir ds/models
RUN mkdir ds/punkt
RUN mkdir ds/modelapi

# copy the files over
COPY requirements.txt /ds
COPY setup.cfg /ds
COPY setup.py /ds
COPY main.py /ds
COPY modelapi /ds/modelapi
COPY models/weighted_svm.joblib /ds/models


WORKDIR /ds
# install dependencies first
RUN pip install -r requirements.txt
RUN python setup.py install
RUN python modelapi/install_nltk.py

CMD ["uvicorn", "--workers","2", "--host","0.0.0.0", "--port", "8080","main:app"]
