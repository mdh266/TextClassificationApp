import pandas as pd
from imblearn.pipeline import Pipeline 
from sklearn.metrics import (classification_report,
                             balanced_accuracy_score)

def evaluate_model(
    train_df : pd.DataFrame,
    test_df  : pd.DataFrame,
    mapping  : dict,
    pipe     : Pipeline,
) -> None:

    model = pipe.fit(train_df["text"], 
                     train_df["target"])


    pred  = model.predict(test_df["text"])

    print(classification_report(test_df["target"],
                                pred, 
                                target_names=mapping))
    
    print()
    print("balanced_accuracy", balanced_accuracy_score(test_df["target"], 
                                                       pred))