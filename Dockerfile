# Copyright (c) Mike Harmon.
# Distributed under the terms of the Modified BSD License.

FROM jupyter/base-notebook

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
    texlive-generic-recommended \
    texlive-latex-base \
    texlive-latex-extra \
    texlive-xetex \
    unzip \
    vim \
    && apt-get clean && \
    rm -rf /var/lib/apt/lists/*


USER $NB_UID

RUN mkdir /home/$NB_USER/NLP && \
    fix-permissions /home/$NB_USER/NLP


COPY requirements.txt     /home/$NB_USER/NLP
COPY NLP.ipynb            /home/$NB_USER/NLP

RUN pip install -r /home/$NB_USER/NLP/requirements.txt


USER $NB_UID

