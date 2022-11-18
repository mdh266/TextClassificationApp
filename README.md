# Building and Deploying A Text Classification Web App
-----------------

**Web App**: https://docwebapp-j3zdo3lhcq-uc.a.run.app/


## About
------
In this project, over a series of blog posts I'll be buidling a model [document classification](https://en.wikipedia.org/wiki/Document_classification), also known as [text classification](https://monkeylearn.com/text-classification/) and deploying the model as part of a web application to predict the topic of research papers from their abstract.


## 1st Blog Post: Dealing With Imbalanced Data
-----
In the first blog post I will be working with the <a href="http://scikit-learn.org/">Scikit-learn</a> library and an imbalanced dataset (corpus) that I will create from summaries of papers published on [arxiv](https://arxiv.org). The topic of each paper is already labeled as the category therefore alleviating the need for me to label the dataset. The imbalance in the dataset will be caused by the imbalance in the number of samples in each of the categories we are trying to predict. Imbalanced data occurs quite frequently in classification problems and makes developing a good model more challenging. Often times it is too expensive or not possible to get more data on the classes that have to few samples. Developing strategies for dealing with imbalanced data is therefore paramount for creating a good classification model.  I will cover some of the basics of dealing with imbalanced data using the [Imbalance-Learn](https://imbalanced-learn.readthedocs.io/en/stable/) library as well as building a Naive Bayes classifier and Support Vector Machine using  from <a href="http://scikit-learn.org/">Scikit-learn</a>. I will also over the basics of term frequency-inverse document frequency and visualizing it using the [Plotly](https://plotly.com/python/) library.


## 2nd Blog Post: Using The Natural Language Toolkit 
-----
In this blogpost I picked up from the last one and went over using the [Natural Language Toolkit (NLTK)](https://www.nltk.org/) to improve the performance of our text classification models. Specifically, we went over how to remove stopwords, stemming and lemmitization. I applied each of these to the weighted Support Vector Machine model and performed a grid search to find the optimal parameters to use for our models. Finally I persist our model to disk using [Joblib](https://joblib.readthedocs.io/en/latest/) so that we can use it as part of a rest API.


## 3rd Blog Post: A Machine Learning Powered Web App
-----
In this post we'll build out a serverless web app using a few technologies. The advantage of using a serverless framework for me is cost effectiveness: I don't pay much at all unless people use my web app a ton and I don't expect people to visit this app very often. However, due to the serverless framework I will have issues with latency, which I can live with. I'll first go over how to convert my text classification model from the [last post](http://michael-harmon.com/blog/NLP2.html) into a Rest API using [FastAPI](https://fastapi.tiangolo.com/) and [Joblib](https://joblib.readthedocs.io/en/latest/). Using our model in this way will allow us to send our paper abstracts as [json](https://en.wikipedia.org/wiki/JSON) through an HTTP request and get back the predicted topic label for the paper abstract. After this I'll build out a web application usign [FastAPI](https://fastapi.tiangolo.com/) and [Bootstrap](https://getbootstrap.com/). Using Bootstrap allows us to have a beautiful responsive website without having to write HTML or JavaScript. Finally, I'll go over deploying both the model API and Web app using [Docker](https://www.docker.com/) and [Google Cloud Run](https://cloud.google.com/run) to build out a serverless web application!


## 4th Blog Post:  Deep Learning With Tensorflow & Optuna
-----
This time I will use a [Convolutional Neural Network (CNN)](https://en.wikipedia.org/wiki/Convolutional_neural_network) model with [Tensorflow](https://www.tensorflow.org/) and [Keras](https://keras.io/) to predict the topic of each paper's abstract and use [Optuna](https://optuna.org/) to optimize the hyperparamters of the model. Keras is a high level library that makes building complex deep learning models relatively easy and since it can use [Tensorflow](https://www.tensorflow.org/) as a backend, it is a production ready framework. Optuna is powerful automatic hyperparameter tuning library that uses a *define-by-run* design that makes it elegant and easy to use. I have just started using this library and have been particularly impressed with the design which is extremely intuitve. While CNN's are no longer the state-of-the-art algorithms for text classification, they still perform quite well and I wanted to explore how they would work on this problem. I should note that, the point of this isn't to build the most high performing model, but rather to show how these tools fit together to build an end-to-end deep learning model.


## How To Run This:
------

To use the notebooks in this project first download [Docker](https://www.docker.com/) and then you can start the notebook with the command:

	docker-compose up

and going to the posted url. To recreate the restapi and web app use the commands listed in `modealapi` and `webapp` respectively.s
