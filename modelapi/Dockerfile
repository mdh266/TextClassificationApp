FROM continuumio/miniconda3:4.7.12

# set up file system
RUN mkdir ds
RUN mkdir ds/model
RUN mkdir ds/src

# copy the files over
COPY main.py /ds
COPY setup.cfg /ds
COPY setup.py /ds
COPY requirements.txt /ds
COPY src /ds/src
COPY model/weighted_svm.joblib /ds/model


WORKDIR /ds
# install dependencies first
RUN pip install -r requirements.txt
RUN python setup.py install

CMD ["gunicorn", "-w","2", "-b","0.0.0.0:8080","main:app"]
