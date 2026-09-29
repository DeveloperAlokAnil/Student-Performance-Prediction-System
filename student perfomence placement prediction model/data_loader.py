import pandas as pd

def load_dataset(filename="student_data.csv"):
    """
    Load the student dataset from a CSV file.
    """

    df = pd.read_csv(filename)

    return df
