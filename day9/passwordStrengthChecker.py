# Function to classify password strength
def check_password_strength(password):
    # Check the length first
    if len(password) < 8:
        return "Weak"

    # Flags to check the presence of required characters
    has_upper = False
    has_lower = False
    has_number = False
    has_special = False
    special_characters = "!@#$%^&*(),.?\":{}|<>"

    # Loop through each character in the password and check the conditions
    for char in password:
        if char.isupper():
            has_upper = True
        elif char.islower():
            has_lower = True
        elif char.isdigit():
            has_number = True
        elif char in special_characters:
            has_special = True
    
    # Determine the strength of the password
    if has_upper and has_lower and has_number and has_special:
        return "Strong"
    elif has_upper and has_lower and has_number:
        return "Medium"
    else:
        return "Weak"


# Loop until a strong password is entered
while True:
    password = input("Enter a password: ")
    strength = check_password_strength(password)
    
    if strength == "Strong":
        print(f"Password is {strength}. You have entered a strong password!")
        break
    else:
        print(f"Password is {strength}. Please try again.")
