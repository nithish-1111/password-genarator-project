def analyze_password(password):
    score = 0
    suggestions = []

    if len(password) >= 12:
        score += 1
    else:
        suggestions.append("Use at least 12 characters when possible.")

    if any(c.islower() for c in password):
        score += 1
    else:
        suggestions.append("Add lowercase letters.")

    if any(c.isupper() for c in password):
        score += 1
    else:
        suggestions.append("Add uppercase letters.")

    if any(c.isdigit() for c in password):
        score += 1
    else:
        suggestions.append("Add numbers.")

    if any(not c.isalnum() for c in password):
        score += 1
    else:
        suggestions.append("Add symbols.")

    if score >= 4:
        strength = "Strong"
    elif score >= 3:
        strength = "Medium"
    else:
        strength = "Weak"

    result = f"Strength: {strength}"

    if suggestions:
        result += "\nSuggestions: " + " ".join(suggestions)

    return result
