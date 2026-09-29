from input_handler import get_password_length, get_character_choices
from password_generator import generate_password
from password_analyzer import analyze_password
from file_manager import save_password


def main():
    print("\n=== Secure Password Generator ===")

    while True:
        length = get_password_length()
        choices = get_character_choices()

        password = generate_password(length, choices)

        print("\nGenerated Password:", password)
        print("\nPassword Analysis:")
        print(analyze_password(password))

        save_password(password)

        again = input("\nGenerate another password? (y/n): ").strip().lower()
        if again != "y":
            print("Thank you for using the Password Generator.")
            break


if __name__ == "__main__":
    main()
