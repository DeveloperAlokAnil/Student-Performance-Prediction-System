Student Performance and Placement Prediction System:

 1. Project Title

Student Performance and Placement Prediction System

 2. Overview of the Project

This is a Python-based student prediction system that uses student academic and activity data to:

- Analyze the student dataset.
- Predict a student's final marks using Linear Regression.
- Predict whether a student is likely to be placed using Logistic Regression.
- Calculate the probability of placement.
- Validate student input before using it for prediction.
- Evaluate the performance of the machine-learning models.
- Run automated tests to check dataset loading and input validation.

The system uses the following student information as prediction features:

- Study hours per day
- Attendance percentage
- 10th marks
- 12th marks
- Previous semester marks
- Assignment score
- Internship status
- Number of projects

The dataset also contains `final_marks` and `placed`, which are used as target variables for model training. The main program reads the student dataset, trains both models, accepts new student details, and displays the prediction results.

 3. Features

 Dataset Analysis
- Displays the first five student records.
- Displays the number of rows and columns.
- Displays column names and dataset information.
- Generates a statistical summary.
- Checks for missing values.
- Checks for duplicate rows.

 Performance Prediction
- Uses Linear Regression to predict final marks.
- Uses the following evaluation metrics:
  - Mean Absolute Error (MAE)
  - Mean Squared Error (MSE)
  - Root Mean Squared Error (RMSE)
  - R² Score

 Placement Prediction
- Uses Logistic Regression to predict placement status.
- Predicts:
  - `Placed`
  - `Not Placed`
- Calculates placement probability.
- Evaluates the model using:
  - Accuracy
  - Confusion Matrix
  - Precision
  - Recall
  - F1 Score

 Student Input
The program accepts new student information interactively through the terminal.

 Input Validation
The validation module checks that:
- Study hours are not negative.
- Attendance is between 0 and 100.
- 10th marks are between 0 and 100.
- 12th marks are between 0 and 100.
- Previous semester marks are between 0 and 100.
- Assignment score is between 0 and 100.
- Internship is either `0` or `1`.
- Number of projects is not negative.

 Automated Testing
The project includes unit tests for:
- Dataset loading.
- Dataset row count.
- Required columns.
- Missing values.
- Valid student data.
- Invalid attendance.
- Invalid marks.
- Invalid internship input.

 4. Technologies / Tools Used

 Programming Language
- Python 3

 Libraries
- Pandas – loading and processing CSV data.
- Scikit-learn – machine-learning models and evaluation metrics.
- unittest – automated testing.

 Machine Learning Algorithms
- Linear Regression – final marks prediction.
- Logistic Regression – placement prediction.

 Data Format
- CSV (`student_data.csv`)

 Development Tools
The project can be run using:
- Command Prompt / Terminal
- VS Code
- PyCharm
- Any Python-compatible IDE

 5. Project Structure

```text
Student-Prediction-System/
│
├── main.py
├── data_loader.py
├── data_analysis.py
├── performance_model.py
├── placement_model.py
├── prediction.py
├── result.py
├── validation.py
├── visualization.py
├── test_system.py
├── student_data.csv
└── README.md
```

 Module Description

| File | Purpose |
|---|---|
| `main.py` | Main program containing the complete dataset processing, model training, prediction, evaluation, and user-input workflow. |
| `data_loader.py` | Loads the student dataset using Pandas. |
| `data_analysis.py` | Provides functions for dataset inspection, statistics, missing-value checks, and duplicate checks. |
| `performance_model.py` | Provides functions for training, predicting, and evaluating the Linear Regression performance model. |
| `placement_model.py` | Provides functions for training, predicting, evaluating, and calculating placement probability using Logistic Regression. |
| `prediction.py` | Collects student information from the user and creates a Pandas DataFrame for prediction. |
| `result.py` | Displays predicted final marks, placement result, and placement probability. |
| `validation.py` | Validates student input values. |
| `visualization.py` | Contains the visualization module placeholder/function. |
| `test_system.py` | Contains automated unit tests for the system. |
| `student_data.csv` | Dataset used to train and test the prediction models. |

 6. Steps to Install & Run the Project

 Step 1: Install Python

Install Python 3 on your computer.

Check whether Python is installed:

```bash
python --version
```

or:

```bash
python3 --version
```

 Step 2: Create / Open the Project Folder

Place all Python files and the CSV dataset in the same project folder.

Make sure the dataset is named:

```text
student_data.csv
```

> The uploaded dataset may have a different filename such as `student_data(1).csv`. Rename it to `student_data.csv` before running the current program because the code expects that filename.

 Step 3: Install Required Libraries

Open a terminal inside the project folder and run:

```bash
pip install pandas scikit-learn
```

If your system uses `pip3`:

```bash
pip3 install pandas scikit-learn
```

`unittest` is included with Python, so it does not need to be installed separately.

 Step 4: Run the Main Program

Run:

```bash
python main.py
```

The program will:

1. Load the student dataset.
2. Analyze the dataset.
3. Split the data into training and testing sets.
4. Train the Linear Regression performance model.
5. Evaluate the performance model.
6. Train the Logistic Regression placement model.
7. Evaluate the placement model.
8. Ask the user to enter student details.
9. Predict final marks.
10. Predict placement status.
11. Display placement probability.

 Step 5: Enter Student Details

The program asks for:

```text
Study hours per day:
Attendance percentage:
10th marks:
12th marks:
Previous semester marks:
Assignment score:
Internship (1 = Yes, 0 = No):
Number of projects:
```

Example input:

```text
Study hours per day: 6
Attendance percentage: 85
10th marks: 80
12th marks: 82
Previous semester marks: 78
Assignment score: 88
Internship (1 = Yes, 0 = No): 1
Number of projects: 3
```

The program then displays:

```text
PREDICTION RESULT

Predicted Final Marks: ...
Placement Prediction: Placed / Not Placed
Placement Probability: ... %
```

 7. Instructions for Testing

The project contains automated tests in:

```text
test_system.py
```

 Run All Tests

From the project folder, run:

```bash
python -m unittest test_system.py
```

You can also use:

```bash
python test_system.py
```

 Tests Included

The test suite checks:

1. Dataset Loading
   - Confirms that the dataset can be loaded successfully.

2. Dataset Row Count
   - Confirms that the dataset contains 100 rows.

3. Required Columns
   - Checks that all required student and target columns are present.

4. Missing Values
   - Checks that the dataset contains no missing values.

5. Valid Student Data
   - Checks that valid student input is accepted.

6. Invalid Attendance
   - Checks that attendance above 100 is rejected.

7. Invalid Marks
   - Checks that marks above 100 are rejected.

8. Invalid Internship
   - Checks that an internship value other than `0` or `1` is rejected.

 Expected Test Result

A successful test run should show output similar to:

```text
........
----------------------------------------------------------------------
Ran 8 tests in ...s

OK
```

The exact execution time may vary between computers.

 8. Input Validation Rules

| Input | Valid Range / Format |
|---|---|
| Study hours | 0 or greater |
| Attendance | 0–100 |
| 10th marks | 0–100 |
| 12th marks | 0–100 |
| Previous semester marks | 0–100 |
| Assignment score | 0–100 |
| Internship | `0` or `1` |
| Projects | 0 or greater |

 9. Important Note

The prediction results are generated from the provided student dataset and machine-learning models. They should be treated as model predictions rather than guaranteed academic or placement outcomes.

Screenshot:
<img width="1855" height="875" alt="image" src="https://github.com/user-attachments/assets/c2356d26-e43e-4118-917c-33ca5910cbd1" />
