def precedence(op):
    if op == '+' or op == '-':
        return 1
    if op == '*' or op == '/':
        return 2
    if op == '^':
        return 3
    return 0

def infix_to_postfix(expression):
    stack = []
    postfix = ""

    for ch in expression:
        # If operand, add to postfix
        if ch.isalnum():     # whether a character (or string) is alphanumeric.
            postfix += ch

        # If '(', push to stack
        elif ch == '(':
            stack.append(ch)

        # If ')', pop until '('
        elif ch == ')':
            while stack and stack[-1] != '(':
                postfix += stack.pop()
            stack.pop()  # remove '('

        # Operator
        else:
            while (stack and precedence(ch) <= precedence(stack[-1])):
                postfix += stack.pop()
            stack.append(ch)

    # Pop remaining operators
    while stack:
        postfix += stack.pop()

    return postfix

# User input
infix = input("Enter Infix Expression: ")
print("Postfix Expression:", infix_to_postfix(infix))