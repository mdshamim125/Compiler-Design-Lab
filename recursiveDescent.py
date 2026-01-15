# ------------------------------------
# Recursive Descent Parser
# Grammar implemented:
#
#   E  → T E'
#   E' → + T E' | - T E' | ε
#   T  → F T'
#   T' → * F T' | / F T' | ε
#   F  → a | b | c
#
# ------------------------------------

# Read input expression from user
# Spaces are removed to simplify parsing
# Example input: a+b*c
input_string = input("Enter the input symbol: ").replace(" ", "")

# Append end-of-input marker
input_string += "$"

# Index pointer to track current character in input
i = 0

# ------------------------------------
# Error handling function
# ------------------------------------
def error():
    print("String is NOT accepted")
    exit()  # Stop execution immediately

# ------------------------------------
# Match function
# ------------------------------------
# Checks whether the current input symbol
# matches the expected character
def match(ch):
    global i
    if input_string[i] == ch:
        i += 1        # Move to next character
    else:
        error()

# ------------------------------------
# E → T E'
# ------------------------------------
# Parses an expression
def E():
    T()              # Parse first term
    E_prime()        # Parse remaining + or - parts

# ------------------------------------
# E' → + T E' | - T E' | ε
# ------------------------------------
# Handles addition and subtraction
def E_prime():
    # If next symbol is + or -, consume it
    if input_string[i] in ['+', '-']:
        match(input_string[i])  # Match operator
        T()                     # Parse next term
        E_prime()               # Handle further + or -
    return                      # ε (empty production)

# ------------------------------------
# T → F T'
# ------------------------------------
# Parses a term
def T():
    F()              # Parse factor
    T_prime()        # Parse remaining * or / parts

# ------------------------------------
# T' → * F T' | / F T' | ε
# ------------------------------------
# Handles multiplication and division
def T_prime():
    # If next symbol is * or /, consume it
    if input_string[i] in ['*', '/']:
        match(input_string[i])  # Match operator
        F()                     # Parse next factor
        T_prime()               # Handle further * or /
    return                      # ε (empty production)

# ------------------------------------
# F → a | b | c
# ------------------------------------
# Parses a factor (operand)
def F():
    # Accept any valid operand
    if input_string[i] in ['a', 'b', 'c']:
        match(input_string[i])
    else:
        error()

# ------------------------------------
# Start parsing from the start symbol
# ------------------------------------
E()

# After parsing, input must be fully consumed
if input_string[i] == '$':
    print("String is accepted")
else:
    print("String is NOT accepted")
