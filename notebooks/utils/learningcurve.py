import matplotlib.pyplot as plt
from typing import List
import numpy as np
import plotly.graph_objects as go


def plot_learning_curve(
    train_sizes  : List[int], 
    train_scores : List[float], 
    test_scores  : List[float]
) -> None:
    """
    adapted from:
        https://scikit-learn.org/stable/auto_examples/model_selection/plot_learning_curve.html
    """
    train_scores_mean = np.mean(train_scores, axis=1)
    train_scores_std = np.std(train_scores, axis=1)
    test_scores_mean = np.mean(test_scores, axis=1)
    test_scores_std = np.std(test_scores, axis=1)

    fig = go.Figure()

    fig.add_trace(go.Scatter(
                    x=train_sizes, 
                    y=train_scores_mean - train_scores_std,
                    fill=None,
                    showlegend=False,
                    mode='lines',
                    hoverinfo='skip',
                    line_color='indigo',
                    opacity=0.0,
                    ))

    fig.add_trace(go.Scatter(
                  x=train_sizes, 
                  y=train_scores_mean + train_scores_std,
                  showlegend=False,
                  fill='tonexty', # fill area between trace0 and trace1
                  mode='lines', 
                  hoverinfo='skip',
                  opacity=0.0,
                  line_color='indigo'))

    fig.add_trace(go.Scatter(
                    x=train_sizes, 
                    y=train_scores_mean,
                    fill=None,
                    mode='lines',
                    name="Train",
                    line_color='indigo',
                    ))

    fig.add_trace(go.Scatter(
                    x=train_sizes, 
                    y=test_scores_mean - test_scores_std,
                    fill=None,
                    showlegend=False,
                    mode='lines',
                    hoverinfo='skip',
                    line_color='blue',
                    ))

    fig.add_trace(go.Scatter(
                  x=train_sizes, 
                  y=test_scores_mean + test_scores_std,
                  fill='tonexty', # fill area between trace0 and trace1
                  mode='lines', 
                  showlegend=False,
                  opacity=0.2,
                  hoverinfo='skip',
                  line_color='blue'))

    fig.add_trace(go.Scatter(
                    x=train_sizes, 
                    y=test_scores_mean,
                    fill=None,
                    mode='lines',
                    line_color='blue',
                    name="Test"
                    ))

    fig.update_layout(title='Learning Curve',
                      font_size=12,
                      height=500,
                      width=700)

    fig.update_xaxes(title='Training Corpus Size')
    fig.update_yaxes(title='Balanced Accuracy')

    fig.show()