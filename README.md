# Document Classification With Natural Language Processing
-----------------

## About
In this blog post we covered document classification using <a href="http://scikit-learn.org/">Scikit-learn</a> and the <a href="http://qwone.com/~jason/20Newsgroups/">20 News Groups</a> dataset. We went over the basics of term frequency-inverse document frequency, pipelines and the Naive Bayes classifier


## Using Notebook
-----------------

You can install the dependencies and access the notebook using <a href="https://www.docker.com/">Docker</a> by building the Docker image with the following:


	docker built -t doc_class .

Followed by running the caommand container:

	docker run -p 8888:8888 -t doc_class


See <a href="https://jupyter-docker-stacks.readthedocs.io/en/latest/index.html">here</a> for more info.  Otherwise in addition to Python 3.5 and Jupyter notebooks, install the additional libraries listed in <code>requirements.txt</code> which can be installed with the command,

	pip install -r requirements.txt

	