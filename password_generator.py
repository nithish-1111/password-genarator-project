import secrets
import string


def generate_password(length, choices):
    character_sets = []

    if choices["lowercase"]:
        character_sets.append(string.ascii_lowercase)
    if choices["uppercase"]:
        character_sets.append(string.ascii_uppercase)
    if choices["numbers"]:
        character_sets.append(string.digits)
    if choices["symbols"]:
        character_sets.append(string.punctuation)

    # Guarantee at least one character from every selected category.
    password = [secrets.choice(charset) for charset in character_sets]

    all_characters = "".join(character_sets)

    while len(password) < length:
        password.append(secrets.choice(all_characters))

    secrets.SystemRandom().shuffle(password)
    return "".join(password)
