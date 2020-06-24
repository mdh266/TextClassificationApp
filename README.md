# Document Classification With Natural Language Processing
-----------------

## About
------
Natural language processing (NLP) is an hot topic in data science and machine learning.  While research in NLP dates back to the 1950's, the real revolution in this domain came in 1980's and 1990's with the introduction of statistical models and fast computational power. Before this most language processing tasks made use of hand-coded rules which were generally not very robust.

The span of topics in Natural Language Processing is immense and I'll just getting to the tip of the iceberg with the topic of [document classification](https://en.wikipedia.org/wiki/Document_classification), also known as [text classification](https://monkeylearn.com/text-classification/). I will be working with the <a href="http://scikit-learn.org/">Scikit-learn</a> library and an imbalanced dataset (corpus) that I will create from summaries of papers published on [arxiv](https://arxiv.org). The topic of each paper is already labeled as the category therefore alleviating the need for me to label the dataset. The imbalance in the dataset will be caused by the imbalance in the number of samples in each of the categories we are trying to predict. Imbalanced data occurs quite frequently in classification problems and makes developing a good model more challenging. Often times it is too expensive or not possible to get more data on the classes that have to few samples. Developing strategies for dealing with imbalanced data is therefore paramount for creating a good classification model.  We will cover some of the basics of dealing with imbalanced data using the [Imbalance-Learn](https://imbalanced-learn.readthedocs.io/en/stable/) library.  We will also over the basics of term frequency-inverse document frequency, stop words, lemmatization using the [NLTK](https://www.nltk.org/) as well as using Naive Bayes classifier from <a href="http://scikit-learn.org/">Scikit-learn</a>.


## Using:
------

To use the notebooks in this project first download [Docker](https://www.docker.com/) and then you can start the notebook with the command:

	docker-compose up

and going to the posted url.
