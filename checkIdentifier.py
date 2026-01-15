# Import keyword module to check reserved words
# Import re module for regular expression matching
import keyword
import re

# Function to check whether a string is a valid identifier
def is_identifier(s):
    # Regular expression rule for identifiers:
    # Must start with a letter or underscore
    # Followed by letters, digits, or underscores
    pattern = r"^[A-Za-z_][A-Za-z0-9_]*$"

    # Check:
    # 1. Matches identifier pattern
    # 2. Is NOT a reserved keyword
    if re.match(pattern, s) and not keyword.iskeyword(s):
        return True
    return False

# List of test tokens taken from a source program
tests = ["var1", "_temp", "2ndvar", "Hello_world", "a$s", "if", "for"]

# Check each token and display result
for test in tests:
    if is_identifier(test):
        print(f"'{test}' is a valid identifier")
    else:
        print(f"'{test}' is not a valid identifier")