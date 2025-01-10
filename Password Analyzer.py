import re
from colorama import Fore, Style  # type: ignore # Correctly import Fore and Style

# Function to evaluate password strength
def analyze_password(password):
    strength = 0
    recommendations = []

    # Length check
    if len(password) < 8:
        recommendations.append("Increase the length of your password (at least 8 characters).")
    else:
        strength += 1

    # Character variety check
    if not re.search(r'[A-Z]', password):
        recommendations.append("Add at least one uppercase letter.")
    else:
        strength += 1

    if not re.search(r'[a-z]', password):
        recommendations.append("Add at least one lowercase letter.")
    else:
        strength += 1

    if not re.search(r'\d', password):
        recommendations.append("Include at least one numeric digit.")
    else:
        strength += 1

    if not re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        recommendations.append("Include at least one special character (!@#$%^&*(), etc.).")
    else:
        strength += 1

    # Common patterns check
    if re.search(r'(.)\1{2,}', password):
        recommendations.append("Avoid using repeated sequences of the same character.")

    if password.lower() in ["password", "123456", "qwerty", "letmein"]:
        recommendations.append("Avoid using common or easily guessed passwords.")

    # Strength evaluation
    if strength <= 2:
        return Fore.RED + "Weak" + Style.RESET_ALL, recommendations
    elif strength == 3:
        return Fore.YELLOW + "Medium" + Style.RESET_ALL, recommendations
    else:
        return Fore.GREEN + "Strong" + Style.RESET_ALL, recommendations

# Main function
def main():
    print("=== Password Analyzer ===")
    password = input("Enter a password to analyze: ")
    strength, tips = analyze_password(password)

    print(f"\nPassword Strength: {strength}")
    if tips:
        print("\nRecommendations to improve your password:")
        for tip in tips:
            print(f"- {tip}")
    else:
        print("Your password is strong!")

if __name__ == "__main__":
    main()
