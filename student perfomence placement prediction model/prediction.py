import pandas as pd


def get_student_input():

    print("\n==========================================")
    print("       STUDENT PREDICTION SYSTEM")
    print("==========================================")

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

    student = pd.DataFrame(
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

    return student
