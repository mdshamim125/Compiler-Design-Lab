# Function to determine operator precedence
def precedence(op):
    """
    Returns precedence level of an operator.
    Higher number => higher precedence.
    """
    if op == '+' or op == '-':
        return 1
    if op == '*' or op == '/':
        return 2
    if op == '^':
        return 3
    return 0  # Non-operators


# Function to convert infix expression to postfix
def infix_to_postfix(expression):
    """
    Converts an infix expression (like a+b*c) to postfix (like abc*+)
    using a stack-based algorithm.
    """
    stack = []    # Stack to hold operators and parentheses
    postfix = ""  # Output string for postfix expression

    for ch in expression:
        if ch.isalnum():  # If the character is an operand (letter or digit)
            postfix += ch  # Add it directly to postfix
        elif ch == '(':   # If character is '('
            stack.append(ch)  # Push '(' onto stack
        elif ch == ')':   # If character is ')'
            # Pop all operators from stack until '(' is found
            while stack and stack[-1] != '(':
                postfix += stack.pop()
            stack.pop()  # Remove '(' from stack
        else:  # If character is an operator (+, -, *, /, ^)
            # Pop operators from stack with higher or equal precedence
            while stack and precedence(ch) <= precedence(stack[-1]):
                postfix += stack.pop()
            stack.append(ch)  # Push current operator onto stack

    # Pop remaining operators from the stack
    while stack:
        postfix += stack.pop()

    return postfix  # Return postfix expression as a string


# Function to generate quadruples from infix expression
def generate_quadruples(expression):
    """
    Generates quadruples (three-address code) from an infix expression.
    Each quadruple has the form: (operator, operand1, operand2, result)
    """
    # Step 1: Convert infix to postfix expression
    postfix = infix_to_postfix(expression)

    stack = []       # Stack to hold operands and intermediate results
    temp_count = 1   # Counter for temporary variables t1, t2, ...
    quadruples = []  # List to store quadruples

    # Step 2: Process each character in postfix expression
    for token in postfix:
        if token.isalnum():  # If token is an operand
            stack.append(token)  # Push operand onto stack
        else:  # Token is an operator
            # Pop top two operands from stack for the operation
            op2 = stack.pop()
            op1 = stack.pop()

            # Create a temporary variable to store result
            temp = f"t{temp_count}"
            temp_count += 1

            # Create quadruple: (operator, operand1, operand2, result)
            quadruples.append((token, op1, op2, temp))

            # Push the temporary variable back onto stack
            stack.append(temp)

    return quadruples  # Return list of quadruples


# Example usage
expr = "a+b+c*d/e+f"  # Infix expression

# Generate quadruples
quads = generate_quadruples(expr)

# Display quadruples in a tabular format
print(f"{'Op':<5}{'Arg1':<5}{'Arg2':<5}{'Result':<5}")
for op, arg1, arg2, res in quads:
    print(f"{op:<5}{arg1:<5}{arg2:<5}{res:<5}")