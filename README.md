# Secure Password Generator

## Overview
A simple console-based Python project that generates secure random passwords and gives basic strength feedback.

## Functional Modules
1. Password Configuration - accepts length and character-type choices.
2. Password Generation - creates a random password using Python's `secrets` module.
3. Password Analysis & Saving - checks basic strength and optionally saves the generated password.

## Technologies
- Python 3
- Python standard library
- Git/GitHub for version control

## Project Structure
- `main.py` - controls the program flow.
- `input_handler.py` - handles user input and validation.
- `password_generator.py` - generates passwords.
- `password_analyzer.py` - analyzes password strength.
- `file_manager.py` - optionally saves the generated password.
- `docs/` - project documentation and diagrams.

## How to Run
Open the project in PyCharm or VS Code and run:

```bash
python main.py
```

No external packages are required.

## Testing
The program can be manually tested using valid and invalid lengths, different character selections, and save/no-save choices.
