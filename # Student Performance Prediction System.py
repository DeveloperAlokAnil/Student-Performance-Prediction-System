# Student Performance Prediction System
# Basic Python - No external libraries

print("======================================")
print("  STUDENT PERFORMANCE PREDICTION")
print("======================================")

# Get student details
name = input("Enter student name: ")

study_hours = float(input("Enter study hours per day: "))
attendance = float(input("Enter attendance percentage: "))
previous_marks = float(input("Enter previous exam marks: "))

# Calculate performance score
study_score = study_hours * 5

if study_score > 100:
    study_score = 100

performance = (
    study_score * 0.30 +
    attendance * 0.30 +
    previous_marks * 0.40
)

# Display result
print("\n========== RESULT ==========")

print("Student Name:", name)
print("Study Hours:", study_hours)
print("Attendance:", attendance, "%")
print("Previous Marks:", previous_marks)

print("Predicted Performance:",
      round(performance, 2), "%")

# Performance category
if performance >= 75:
    print("Performance Level: Excellent")

elif performance >= 60:
    print("Performance Level: Good")

elif performance >= 50:
    print("Performance Level: Average")

else:
    print("Performance Level: Needs Improvement")

print("============================")