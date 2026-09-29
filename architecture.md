# System Architecture

The project uses a simple procedural modular architecture.

User
  ↓
main.py
  ↓
input_handler.py
  ↓
password_generator.py
  ↓
password_analyzer.py
  ↓
file_manager.py

## Components
- Input Handler: validates password length and character choices.
- Password Generator: creates the random password.
- Password Analyzer: gives basic strength feedback.
- File Manager: optionally saves the generated password.
- Main Controller: coordinates the workflow.

This design keeps the project simple while separating major responsibilities into meaningful modules.
