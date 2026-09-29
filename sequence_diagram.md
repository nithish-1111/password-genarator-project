# Sequence Diagram

```text
User -> main.py: Enter requirements
main.py -> input_handler.py: Validate input
input_handler.py -> main.py: Valid choices
main.py -> password_generator.py: Generate password
password_generator.py -> main.py: Return password
main.py -> password_analyzer.py: Analyze password
password_analyzer.py -> main.py: Return strength
main.py -> file_manager.py: Save if requested
file_manager.py -> main.py: Save result
main.py -> User: Display result
```
