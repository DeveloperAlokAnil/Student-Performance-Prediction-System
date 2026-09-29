import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression, LogisticRegression
from sklearn.metrics import (mean_absolute_error,mean_squared_error,r2_score,accuracy_score,confusion_matrix,precision_score,recall_score,f1_score)

df = pd.read_csv("student_data.csv")

print("\n--- First 5 Students ---")
print(df.head())

print("\n--- Dataset Shape ---")
print("Rows and Columns:", df.shape)

print("\n--- Column Names ---")
print(df.columns.tolist())

print("\n--- Dataset Information ---")
df.info()

print("\n--- Statistical Summary ---")
print(df.describe())

print("\n--- Missing Values ---")
print(df.isnull().sum())

print("\n--- Duplicate Rows ---")
print("Number of duplicate rows:", df.duplicated().sum())

X = df[["study_hours","attendance","tenth_marks","twelfth_marks","previous_marks","assignment_score","internship","projects"]]

y_performance = df["final_marks"]


y_placement = df["placed"]

X_train_perf, X_test_perf, y_train_perf, y_test_perf = train_test_split(
    X,
    y_performance,
    test_size=0.2,
    random_state=42
)


X_train_place, X_test_place, y_train_place, y_test_place = train_test_split(
    X,
    y_placement,
    test_size=0.2,
    random_state=42,
    stratify=y_placement
)

print("\n--- Performance Prediction Data ---")
print("Training samples:", len(X_train_perf))
print("Testing samples:", len(X_test_perf))

print("\n--- Placement Prediction Data ---")
print("Training samples:", len(X_train_place))
print("Testing samples:", len(X_test_place))

performance_model = LinearRegression()

performance_model.fit(
    X_train_perf,
    y_train_perf
)

performance_predictions = performance_model.predict(
    X_test_perf
)

print("\n--- Performance Predictions ---")

for actual, predicted in zip(
    y_test_perf,
    performance_predictions
):

    print(
        "Actual:",
        actual,
        "Predicted:",
        round(predicted, 2)
    )

mae = mean_absolute_error(
    y_test_perf,
    performance_predictions
)

mse = mean_squared_error(
    y_test_perf,
    performance_predictions
)

rmse = mse ** 0.5

r2 = r2_score(
    y_test_perf,
    performance_predictions
)

print("\n--- Performance Model Evaluation ---")

print(
    "Mean Absolute Error (MAE):",
    round(mae, 2)
)

print(
    "Mean Squared Error (MSE):",
    round(mse, 2)
)

print(
    "Root Mean Squared Error (RMSE):",
    round(rmse, 2)
)

print(
    "R2 Score:",
    round(r2, 2)
)


placement_model = LogisticRegression(max_iter=1000)

placement_model.fit(
    X_train_place,
    y_train_place
)

placement_predictions = placement_model.predict(
    X_test_place
)

print("\n--- Placement Predictions ---")

for actual, predicted in zip(
    y_test_place,
    placement_predictions
):

    actual_status = (
        "Placed"
        if actual == 1
        else "Not Placed"
    )

    predicted_status = (
        "Placed"
        if predicted == 1
        else "Not Placed"
    )

    print(
        "Actual:",
        actual_status,
        "| Predicted:",
        predicted_status
    )

accuracy = accuracy_score(
    y_test_place,
    placement_predictions
)

confusion = confusion_matrix(
    y_test_place,
    placement_predictions
)

precision = precision_score(
    y_test_place,
    placement_predictions,
    zero_division=0
)

recall = recall_score(
    y_test_place,
    placement_predictions,
    zero_division=0
)

f1 = f1_score(
    y_test_place,
    placement_predictions,
    zero_division=0
)


print("\n--- Placement Model Evaluation ---")

print(
    "Accuracy:",
    round(accuracy, 2)
)

print("\nConfusion Matrix:")
print(confusion)

print("Precision:",round(precision, 2))


print(
    "Recall:",
    round(recall, 2)
)

print(
    "F1 Score:",
    round(f1, 2)
)

print("~" * 40)
print("       STUDENT PREDICTION SYSTEM")
print("~" * 40)

print("\nEnter the following student details:\n")

study_hours = float(
    input("Study hours per day: ")
)

attendance = float(
    input("Attendance percentage: ")
)

tenth_marks = float(
    input("10th marks: ")
)


twelfth_marks = float(
    input("12th marks: ")
)

previous_marks = float(
    input("Previous semester marks: ")
)


assignment_score = float(
    input("Assignment score: ")
)

internship = int(
    input("Internship (1 = Yes, 0 = No): ")
)

projects = int(
    input("Number of projects: ")
)

student_input = pd.DataFrame(
    [[
        study_hours,
        attendance,
        tenth_marks,
        twelfth_marks,
        previous_marks,
        assignment_score,
        internship,
        projects
    ]],
    columns=[
        "study_hours",
        "attendance",
        "tenth_marks",
        "twelfth_marks",
        "previous_marks",
        "assignment_score",
        "internship",
        "projects"
    ]
)

predicted_marks = performance_model.predict(
    student_input
)[0]

placement_result = placement_model.predict(
    student_input
)[0]

placement_probability = placement_model.predict_proba(
    student_input
)[0][1]

print("~" *  40)
print("          PREDICTION RESULT")
print("~" * 40)

print(
    "\nPredicted Final Marks:",
    round(predicted_marks, 2)
)

if placement_result == 1:

    print("Placement Prediction: Placed")

else:

    print("Placement Prediction: Not Placed")


print("Placement Probability:",round(placement_probability * 100, 2),"%")

print("\n==========================================")
