from pathlib import Path


def save_password(password):
    choice = input("Save this password to a text file? (y/n): ").strip().lower()

    if choice == "y":
        Path("generated_password.txt").write_text(password, encoding="utf-8")
        print("Password saved to generated_password.txt")
    else:
        print("Password was not saved.")
