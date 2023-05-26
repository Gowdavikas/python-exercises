credit_score = int(input("Enter credit score : "))

if credit_score < 400 or credit_score >= 850:
    print("Invalid credit score....")
else:
    if 400 <= credit_score < 600:
        print("Congrats!!! You won a Silver Card.")
    elif 600 <= credit_score < 800:
        print("Congrats!!! You won a Golden Card.")
    else:
        print("Congrats!!! You won a Platinum Card.")
