from sklearn.linear_model import LogisticRegression

from sklearn.metrics import (
    accuracy_score,
    confusion_matrix,
    precision_score,
    recall_score,
    f1_score
)


def train_placement_model(X_train, y_train):

    model = LogisticRegression(max_iter=1000)
    model.fit(X_train,y_train)

    return model

def predict_placement(model, X_test):

    predictions = model.predict(X_test)
    return predictions


def evaluate_placement(y_test, predictions):

    accuracy = accuracy_score(
        y_test,
        predictions
    )

    confusion = confusion_matrix(
        y_test,
        predictions
    )

    precision = precision_score(
        y_test,
        predictions,
        zero_division=0
    )

    recall = recall_score(
        y_test,
        predictions,
        zero_division=0
    )

    f1 = f1_score(
        y_test,
        predictions,
        zero_division=0
    )

    return (accuracy,confusion,precision,recall,f1)


def get_placement_probability(model, student):

    probability = model.predict_proba(student)[0][1]
    return probability    
        

    
