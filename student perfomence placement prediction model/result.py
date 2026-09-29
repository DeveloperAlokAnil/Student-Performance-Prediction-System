def display_prediction_result( predicted_marks,placement_result,placement_probability):

    print("\n==========================================")
    print("          PREDICTION RESULT")
    print("==========================================")

    print(
        "\nPredicted Final Marks:",
        round(predicted_marks, 2)
    )

    if placement_result == 1:
        print("Placement Prediction: Placed")
    else:
        print("Placement Prediction: Not Placed")

    print(
        "Placement Probability:",
        round(placement_probability * 100, 2),
        "%"
    )

    print("\n==========================================")
