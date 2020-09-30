# Copyright (c) Mike Harmon.
# Distributed under the terms of the Modified BSD License.

FROM jupyter/base-notebook:python-3.7.6

LABEL maintainer="Jupyter Project <jupyter@googlegroups.com>"

USER root

# Install all OS dependencies for fully functional notebook server
RUN apt-get update && apt-get install -yq --no-install-recommends \
    build-essential \
    git \
    libsm6 \
    libxext-dev \
    libxrender1 \
    lmodern \
    netcat \
    texlive-fonts-extra \
    texlive-fonts-recommended \
    texlive-latex-base \
    texlive-latex-extra \
    texlive-xetex \
    unzip \
    vim \
    && apt-get clean && \
    rm -rf /var/lib/apt/lists/*


USER $NB_UID

RUN mkdir /home/$NB_USER/NLP/ && \
    fix-permissions /home/$NB_USER

WORKDIR /home/$NB_USER/NLP/

RUN git config --global user.email "mdh266@gmail.com" && \
    git config --global user.name "Mike Harmon" 

COPY requirements.txt /home/$NB_USER/NLP/ 

RUN pip install -r /home/$NB_USER/NLP/requirements.txt

RUN jupyter labextension install jupyterlab-plotly@4.10.0

# Import matplotlib the first time to build the font cache.
ENV XDG_CACHE_HOME /home/$NB_USER/.cache/ 
RUN MPLBACKEND=Agg python -c "import matplotlib.pyplot" && \
    fix-permissions /home/$NB_USER

USER $NB_UID
