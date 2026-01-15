# -------------------------------
# Token-based Shift Reduce Parser
# -------------------------------

# Grammar productions
# Each production is written as:
#   (Left Hand Side, Right Hand Side)
# This grammar represents simple arithmetic expressions
import re

productions = [
    ("E", ["E", "+", "E"]),   # Expression + Expression
    ("E", ["E", "*", "E"]),   # Expression * Expression
    ("E", ["(", "E", ")"]),   # Expression inside parentheses
    ("E", ["id"])             # Identifier
]

# Take input expression from user
# Example input: id + id * id
user_input = input("Enter the expression (use 'id' for identifiers): ")

# Split input into tokens based on spaces
# input_tokens = user_input.split()

# Tokenize input properly
input_tokens = re.findall(r'id|\+|\*|\(|\)', user_input)

# Append end-of-input marker
input_tokens.append("$")

# Stack used by the shift-reduce parser
stack = []

# Pointer to track the current position in the input tokens
pointer = 0

# Print table header
print("Stack\t\tInput\t\t\tAction")
print("---------------------------------------------------")

# Parsing loop runs until ACCEPT or ERROR
while True:

    # -------------------------------
    # SHIFT operation
    # -------------------------------
    # Move the next input token onto the stack
    if pointer < len(input_tokens):
        stack.append(input_tokens[pointer])  # Push token to stack
        pointer += 1                          # Move input pointer forward
        print(stack, "\t", input_tokens[pointer:], "\tSHIFT")

    # -------------------------------
    # REDUCE operation
    # -------------------------------
    # Try reducing the stack using grammar rules
    reduced = True
    while reduced:
        reduced = False

        # Check each grammar production
        """Iterates over each production rule
            Example:
            lhs = "E"
            rhs = ["id"]
            The parser checks every rule to see if it can reduce something on the stack"""
        for lhs, rhs in productions:
            # If the top of the stack matches RHS of a rule
            #Does the top of the stack match the right-hand side (RHS) of any grammar rule? If yes → reduce it.
            if len(stack) >= len(rhs) and stack[-len(rhs):] == rhs:
                # Remove RHS symbols from stack
                del stack[-len(rhs):]

                # Push LHS symbol onto stack
                stack.append(lhs)

                print(stack, "\t", input_tokens[pointer:], 
                      f"\tREDUCE {lhs} -> {' '.join(rhs)}")

                reduced = True
                break   # Restart checking reductions

    # -------------------------------
    # ACCEPT condition
    # -------------------------------
    # Parsing is successful if:
    #   Stack contains only 'E'
    #   Input is reduced to '$'
    if stack == ["E"] and input_tokens[pointer:] == ["$"]:
        print(stack, "\t", ["$"], "\tACCEPT")
        break

    # -------------------------------
    # ERROR condition
    # -------------------------------
    # If input is finished and no more reductions are possible
    if pointer >= len(input_tokens) and not reduced:
        print("ERROR: Invalid String")
        break
