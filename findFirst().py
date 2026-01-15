# Grammar representation
# ε represents epsilon (empty string)
grammar = {
    "E": ["TE'"],
    "E'": ["+TE'", "ε"],
    "T": ["FT'"],
    "T'": ["*FT'", "ε"],
    "F": ["(E)", "a"]
}

# Dictionary to store FIRST sets
FIRST = {}

# Function to find FIRST of a symbol
def first(symbol):
    # If FIRST already computed, return it
    if symbol in FIRST:
        return FIRST[symbol]

    FIRST[symbol] = set()

    # If symbol is a terminal
    if not symbol.isupper():
        FIRST[symbol].add(symbol)
        return FIRST[symbol]

    # Process each production of the non-terminal
    for production in grammar[symbol]:
        # If production is epsilon
        if production == "ε":
            FIRST[symbol].add("ε")
        else:
            # Scan symbols from left to right
            i = 0
            while i < len(production):
                # Handle non-terminals like E' or T'
                if i + 1 < len(production) and production[i+1] == "'":
                    sym = production[i:i+2]
                    i += 2
                else:
                    sym = production[i]
                    i += 1

                sym_first = first(sym)
                FIRST[symbol].update(sym_first - {"ε"})

                # Stop if epsilon not found
                if "ε" not in sym_first:
                    break
            else:
                FIRST[symbol].add("ε")

    return FIRST[symbol]

# Compute FIRST for all non-terminals
for nt in grammar:
    first(nt)

# Display FIRST sets
print("FIRST Sets:")
for nt in grammar:
    print(f"FIRST({nt}) = {FIRST[nt]}")