import re

def assess_password_strength(password):
    length_error = len(password) < 8
    lowercase_error = not re.search(r"[a-z]", password)
    uppercase_error = not re.search(r"[A-Z]", password)
    digit_error = not re.search(r"\d", password)
    special_char_error = not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password)

    # Count total errors
    errors = sum([length_error, lowercase_error, uppercase_error, digit_error, special_char_error])

    # Determine strength
    if errors == 0:
        strength = "Very Strong"
    elif errors == 1:
        strength = "Strong"
    elif errors == 2:
        strength = "Moderate"
    else:
        strength = "Weak"

    # Provide feedback
    feedback = []
    if length_error:
        feedback.append("🔸 At least 8 characters")
    if lowercase_error:
        feedback.append("🔸 Include lowercase letters")
    if uppercase_error:
        feedback.append("🔸 Include uppercase letters")
    if digit_error:
        feedback.append("🔸 Include digits")
    if special_char_error:
        feedback.append("🔸 Include special characters (e.g., !, @, #)")

    return strength, feedback

def main():
    print("🔐 Password Strength Checker")
    password = input("Enter your password: ")

    strength, feedback = assess_password_strength(password)

    print(f"\nPassword Strength: {strength}")
    if feedback:
        print("Suggestions to improve:")
        for tip in feedback:
            print(tip)
    else:
        print("✅ Your password is strong!")

if __name__ == "__main__":
    main()
