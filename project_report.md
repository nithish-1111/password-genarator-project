# Secure Password Generator - Project Report

## 1. Introduction
The Secure Password Generator is a console-based Python project designed to generate random passwords according to user-selected requirements.

## 2. Problem Statement
Weak and predictable passwords can reduce account security. The project provides a simple way to create random passwords.

## 3. Objectives
- Generate random passwords.
- Allow users to control password length.
- Allow selection of character types.
- Provide basic password-strength feedback.
- Provide optional local saving.

## 4. Functional Requirements
### FR1 - Password Configuration
The system shall accept a password length from 8 to 128 and character-type choices.

### FR2 - Password Generation
The system shall generate a random password using the selected character types.

### FR3 - Password Analysis and Saving
The system shall provide basic strength feedback and allow the user to save the generated password.

## 5. Non-Functional Requirements
- Usability: simple console interaction.
- Security: use Python's `secrets` module for random generation.
- Reliability: validate invalid input.
- Maintainability: separate major functions into meaningful Python modules.
- Error Handling: invalid numeric input is handled without crashing.
- Resource Efficiency: uses only lightweight standard-library operations.

## 6. System Architecture
The project follows a simple procedural modular architecture:
`main.py -> input_handler.py -> password_generator.py -> password_analyzer.py -> file_manager.py`

## 7. Design
### Workflow
The user enters requirements, the program validates them, generates a password, analyzes it, and optionally saves it.

### Use Case
The main actor is the User. The user configures, generates, analyzes, and optionally saves a password.

### Components
Five procedural Python modules are used to separate responsibilities. No OOP is used.

### Data Storage
No database is required. Optional output is stored in a local text file.

## 8. Design Decisions and Rationale
- Python was selected because it is simple and suitable for a first-semester programming project.
- Console input/output keeps the project easy to understand.
- The `secrets` module is used instead of ordinary random generation for password generation.
- The implementation is procedural rather than object-oriented to keep the project appropriate for the intended syllabus level.
- Five meaningful Python files satisfy the project's modular implementation requirement without adding unnecessary complexity.

## 9. Implementation
The implementation contains:
- `main.py`
- `input_handler.py`
- `password_generator.py`
- `password_analyzer.py`
- `file_manager.py`

Each file has one clear responsibility.

## 10. Screenshots / Results
Add screenshots of:
1. Program start and input.
2. Generated password.
3. Password analysis.
4. Optional password-saving result.

## 11. Testing
Manual testing should include:
- Valid password lengths.
- Length below 8.
- Length above 128.
- Non-numeric length.
- No character type selected.
- Different character-type combinations.
- Save and do-not-save options.

Expected result: the program accepts valid input, rejects invalid input with a message, generates a password, displays strength feedback, and saves only when requested.

## 12. Challenges
- Validating user input.
- Ensuring the generated password contains the selected character types.
- Separating the project into simple modules.
- Understanding secure random password generation.

## 13. Learnings
- Python functions and modules.
- Input validation.
- Random password generation.
- Basic file handling.
- Modular project organization.
- Git/GitHub project management.

## 14. Future Enhancements
- Password history management.
- More detailed strength analysis.
- Clipboard support.
- A graphical interface.
- More advanced password policies.

## 15. References
- Python Standard Library documentation.
- Python `secrets` module documentation.
