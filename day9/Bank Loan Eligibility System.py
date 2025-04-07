def check_loan_eligibility():
    # Input: Gather user information
    age = int(input("Enter your age: "))
    salary = float(input("Enter your monthly salary: "))
    credit_score = int(input("Enter your credit score: "))
    
    # Check eligibility
    if age >= 18 and age <= 60:  # Age condition: Must be between 18 and 60
        if salary >= 3000:  # Salary condition: Must be greater than or equal to 3000
            if credit_score >= 650:  # Credit score condition: Must be greater than or equal to 650
                print("You are eligible for the loan!")
            else:
                print("Your credit score is too low. You are not eligible for the loan.")
        else:
            print("Your salary is too low to qualify for the loan.")
    else:
        print("You are not eligible for the loan due to age restrictions.")

# Call the function
check_loan_eligibility()
