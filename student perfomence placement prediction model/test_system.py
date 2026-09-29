import unittest
import pandas as pd
from data_loader import load_dataset
from validation import validate_student_data


class TestStudentPredictionSystem(unittest.TestCase):
 
    def test_dataset_loading(self):
        df = load_dataset("student_data.csv")
        self.assertIsNotNone(df)


    def test_dataset_rows(self):
        df = load_dataset("student_data.csv")
        self.assertEqual(len(df), 100)

    
    def test_required_columns(self):

        df = load_dataset("student_data.csv")
        required_columns = ["study_hours","attendance","tenth_marks","twelfth_marks","previous_marks","assignment_score","internship", "projects","final_marks","placed"]
        for column in required_columns:
            self.assertIn(column, df.columns)

    
    def test_missing_values(self):

        df = load_dataset("student_data.csv")
        self.assertEqual(df.isnull().sum().sum(), 0)

    
    def test_valid_student_data(self):

        result = validate_student_data(
            6,      # study hrs
            85,     # attendance
            80,     # 10th marks
            82,     # 12th marks
            78,     # previous marks
            88,     # assignment score
            1,      # internship
            3       # projects
        )

        self.assertTrue(result)

    
    def test_invalid_attendance(self):

        result = validate_student_data(6,120,80,82,78,88,1,3)
        self.assertFalse(result)

    
    def test_invalid_marks(self):

        result = validate_student_data(6,85,120,82,78,88,1,3)

        self.assertFalse(result)

    
    def test_invalid_internship(self):
        result = validate_student_data(6,85,80,82,78,88,2,3)
        self.assertFalse(result)

if __name__ == "__main__":
    unittest.main()
