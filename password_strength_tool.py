import re

def assess_password_strength(password):
    # Criteria for assessing password strength
    length_criteria = len(password) >= 8
    lowercase_criteria = bool(re.search(r'[a-z]', password))
    uppercase_criteria = bool(re.search(r'[A-Z]', password))
    number_criteria = bool(re.search(r'\d', password))
    special_criteria = bool(re.search(r'[!@#$%^&*(),.?":{}|<>]', password))

    # Feedback messages
    feedback = []
    if length_criteria:
        feedback.append("Good length")
    else:
        feedback.append("Password should be at least 8 characters long")

    if lowercase_criteria:
        feedback.append("Contains lowercase letters")
    else:
        feedback.append("Add some lowercase letters")

    if uppercase_criteria:
        feedback.append("Contains uppercase letters")
    else:
        feedback.append("Add some uppercase letters")

    if number_criteria:
        feedback.append("Contains numbers")
    else:
        feedback.append("Add some numbers")

    if special_criteria:
        feedback.append("Contains special characters")
    else:
        feedback.append("Add some special characters")

    # Assess overall strength
    strength = "Weak"
    criteria_met = sum([length_criteria, lowercase_criteria, uppercase_criteria, number_criteria, special_criteria])
    if criteria_met >= 4:
        strength = "Strong"
    elif criteria_met >= 3:
        strength = "Moderate"

    return strength, feedback

def main():
    password = input("Enter your password: ")
    strength, feedback = assess_password_strength(password)
    
    print(f"Password Strength: {strength}")
    print("Feedback:")
    for comment in feedback:
        print(f"- {comment}")

if __name__ == "__main__":
    main()
