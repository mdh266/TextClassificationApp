

from typing import List
import scipy as sp
from scipy.sparse.csr import csr_matrix
import numpy as np
import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.pipeline import Pipeline
import plotly.express as px

def top_n_tfidfs(
    tfidf      : csr_matrix,
    features   : List[str],
    ids        : List[int], 
    class_name : str,
    top_n      : int
) -> pd.DataFrame:
    
    mean_tfidf = sp.mean(tfidf[ids], axis=0).tolist()[0]
    
    return (pd.DataFrame({"feature":features,"tfidf":mean_tfidf})
              .sort_values("tfidf", ascending=False)
              .iloc[:top_n]
              .assign(class_name=class_name))

def get_top_features(    
    pipe     : Pipeline,
    X        : pd.DataFrame,
    y        : pd.Series,
    vect     : str,
    tfidf    : str,
    top_n    : int = 20
) -> List[pd.DataFrame]:
    
    from sklearn.pipeline import make_pipeline
    
    counter    = pipe.named_steps[vect]
    vectorizer = pipe.named_steps[tfidf]
    features   = counter.get_feature_names()
                                  
    tfidf      = make_pipeline(counter,vectorizer).transform(X)
                                  
    labels     = np.unique(y)
    label_ids  = [np.where(y==label) for label in labels]
    
    return pd.concat([top_n_tfidfs(tfidf, features, ids, label, top_n) 
                      for label, ids in zip(labels,label_ids)], axis=0)


def plot_tfidf(
    pipe     : Pipeline,
    labeler  : LabelEncoder,
    X        : pd.DataFrame,
    y        : pd.Series,
    vect     : str,
    tfidf    : str,
    top_n    : int = 20
) -> None:
    """
    # Adapted from https://buhrmann.github.io/tfidf-analysis.html
    """
    top_n_tfidfs = get_top_features(pipe  = pipe,
                                    X     = X,
                                    y     = y,
                                    vect  = "vect",
                                    tfidf = "tfidf",
                                    top_n = top_n)
    
    top_n_tfidfs = (top_n_tfidfs.assign(
                            class_name=labeler
                                        .inverse_transform(
                                            top_n_tfidfs["class_name"]
                                        ))
    )

    fig = px.bar(top_n_tfidfs, 
                 x='tfidf', 
                 y='feature',
                 facet_col="class_name",
                 facet_col_wrap=2,
                 facet_col_spacing=0.15,
                 height=1000,
                 width=800
                )

    fig.update_yaxes(matches=None)
    fig.update_xaxes(matches=None)
    fig.update_xaxes(showticklabels=True)
    fig.update_yaxes(showticklabels=True)
    
    fig.show()
    


def plot_coefficients(
    pipe       : Pipeline,
    tf_name    : str,
    model_name : str,
    ovr_num    : int,
    title      : str,
    top_n      : int = 10
) -> None:
    """
    Adapted from 
    https://medium.com/@aneesha/visualising-top-features-in-linear-svm-with-scikit-learn-and-matplotlib-3454ab18a14d
    """
    
    features = np.array(pipe.named_steps[tf_name].get_feature_names())
    coef     = pipe.named_steps[model_name].coef_[ovr_num]
    
    top_positive_coefficients = np.argsort(coef)[-top_n:]
    top_negative_coefficients = np.argsort(coef)[:top_n]
    
    top_coefficients = np.hstack([top_negative_coefficients, top_positive_coefficients])
    
    colors = ["positive" if c > 0 else "negative" for c in coef[top_coefficients]]
    
    df = pd.DataFrame({"feature": features[top_coefficients],
                       "Mean t-idf Score": coef[top_coefficients],
                       "influence"  : colors})
    
    fig = px.bar(df, y = "Mean t-idf Score", x ="feature", 
                 title=title,
                 color="influence",
                 category_orders={'influence':['negative','positive']},
                 color_discrete_sequence=['red','blue']
            )

    fig.update_layout(legend_traceorder="reversed")
    fig.show()