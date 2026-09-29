def validate_student_data(study_hours,attendance,tenth_marks,twelfth_marks,previous_marks,assignment_score,internship,projects):

    if study_hours < 0:
        return False
    if attendance < 0 or attendance > 100:
        return False

    if tenth_marks < 0 or tenth_marks > 100:
        return False

    if twelfth_marks < 0 or twelfth_marks > 100:
        return False


    if previous_marks < 0 or previous_marks > 100:
        return False

    if assignment_score < 0 or assignment_score > 100:
        return False

    if internship not in [0, 1]:
        return False

    if projects < 0:
        return False


    return True
