import nltk

if __name__ == "__main__":
	for package in ['stopwords','punkt','wordnet']:
		nltk.download(package,download_dir='/usr/local/share/nltk_data')