from sklearn.linear_model import LinearRegression
from sklearn.metrics import (
    mean_absolute_error,
    mean_squared_error,
    r2_score
)


def train_performance_model(X_train, y_train):

    model = LinearRegression()

    model.fit(X_train, y_train)

    return model


def predict_performance(model, X_test):

    predictions = model.predict(X_test)

    return predictions


def evaluate_performance(y_test, predictions):

    mae = mean_absolute_error(
        y_test,
        predictions
    )

    mse = mean_squared_error(
        y_test,
        predictions
    )

    rmse = mse ** 0.5

    r2 = r2_score(
        y_test,
        predictions
    )

    return mae, mse, rmse, r2
