# Document Classification With Natural Language Processing
-----------------

## About
In this blog post we covered document classification using <a href="http://scikit-learn.org/">Scikit-learn</a> and the <a href="http://qwone.com/~jason/20Newsgroups/">20 News Groups</a> dataset that we have tweaked to be more realistic. The 20 New Groups is collection of almost 20,000 articles on 20 different topics or 'newsgroups' and we will use a subset of the data and tweak the data so that it is imbalanced. Having imbalanced makes the developing a good model more challenging, but it is also more realistic. Imbalanced classes often occur in classification problems and may times it is too expensive or not possible to get more data on the classes that have to few samples. Developing strategies for dealing with imbalanced data is paramount for creating good classification models.  We went over the basics of term frequency-inverse document frequency, stop words, working with imbalanced classes in data, Scikit-leanrn pipelines, and the Naive Bayes classifier.


## Using Notebook
-----------------

You can install the dependencies and access the notebook using <a href="https://www.docker.com/">Docker</a> by building the Docker image with the following:


	docker build -t doc_class .

Followed by running the command container:

	docker run -p 8888:8888 -t doc_class


See <a href="https://jupyter-docker-stacks.readthedocs.io/en/latest/index.html">here</a> for more info.  Otherwise in addition to Python 3.5 and Jupyter notebooks, install the additional libraries listed in <code>requirements.txt</code> which can be installed with the command,

	pip install -r requirements.txt

	
