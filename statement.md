 Project Statement

 1. Problem Statement

Students' academic performance and placement outcomes can be influenced by several factors such as study hours, attendance, previous academic marks, assignment performance, internships, and projects. It can be difficult to evaluate these factors together and estimate a student's expected final marks and placement status manually.

The Student Performance and Placement Prediction System addresses this problem by using student data and machine-learning techniques to provide predictions. The system uses Linear Regression to predict final marks and Logistic Regression to predict placement status and placement probability.

The project also provides dataset analysis, input validation, model evaluation, and automated testing to support the prediction process.

 2. Scope of the Project

The scope of the project includes:

- Loading and analyzing student data from a CSV file.
- Examining the dataset for its structure, statistical information, missing values, and duplicate records.
- Using student academic and activity-related attributes as prediction inputs.
- Training a Linear Regression model for final-mark prediction.
- Training a Logistic Regression model for placement prediction.
- Evaluating the performance model using MAE, MSE, RMSE, and R² Score.
- Evaluating the placement model using accuracy, confusion matrix, precision, recall, and F1 Score.
- Accepting new student information through the terminal.
- Validating student input values before prediction.
- Displaying predicted final marks, placement status, and placement probability.
- Running automated unit tests for important system functions.

The current project is focused on a Python-based, command-line prediction system using the provided student dataset. It does not include a web or mobile interface.

 3. Target Users

The project can be used by:

- Students – to enter their academic and activity information and view model-based predictions.
- Faculty / Teachers – to analyze student data and understand predicted academic and placement outcomes.
- Academic project users – to demonstrate data analysis and machine-learning concepts in a BTech CSE project.
- Developers / Students learning Python and Machine Learning – to study dataset handling, model training, prediction, validation, and testing.

 4. High-Level Features

 4.1 Student Dataset Analysis
- Displays the first five student records.
- Displays dataset dimensions and column names.
- Provides dataset information and statistical summaries.
- Checks for missing values.
- Checks for duplicate records.

 4.2 Academic Performance Prediction
- Uses Linear Regression.
- Predicts the student's final marks.
- Provides MAE, MSE, RMSE, and R² Score for model evaluation.

 4.3 Placement Prediction
- Uses Logistic Regression.
- Predicts whether the student is placed or not placed.
- Calculates placement probability.
- Provides accuracy, confusion matrix, precision, recall, and F1 Score.

 4.4 Student Input and Prediction
- Collects student information through terminal input.
- Creates a structured Pandas DataFrame from the entered information.
- Uses the trained models to generate predictions.

 4.5 Input Validation
- Validates attendance and marks between 0 and 100.
- Prevents negative study hours and project counts.
- Ensures internship input is either `0` or `1`.
- Rejects invalid student data.

 4.6 Automated Testing
- Tests dataset loading.
- Checks the expected dataset row count.
- Checks required columns.
- Checks missing values.
- Tests valid and invalid student inputs.
