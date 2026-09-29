def get_password_length():
    while True:
        try:
            length = int(input("Enter password length (8-128): "))
            if 8 <= length <= 128:
                return length
            print("Please enter a length between 8 and 128.")
        except ValueError:
            print("Please enter a valid number.")


def get_character_choices():
    while True:
        choices = {
            "lowercase": input("Include lowercase letters? (y/n): ").strip().lower() == "y",
            "uppercase": input("Include uppercase letters? (y/n): ").strip().lower() == "y",
            "numbers": input("Include numbers? (y/n): ").strip().lower() == "y",
            "symbols": input("Include symbols? (y/n): ").strip().lower() == "y",
        }

        if any(choices.values()):
            return choices

        print("Select at least one character type.")
