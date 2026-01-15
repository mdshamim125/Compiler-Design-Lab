# Grammar representation
grammar = {
    "E": ["TE'"],
    "E'": ["+TE'", "ε"],
    "T": ["FT'"],
    "T'": ["*FT'", "ε"],
    "F": ["(E)", "a"]
}

# FIRST sets (computed as in your program)
FIRST = {}

def first(symbol):
    if symbol in FIRST:
        return FIRST[symbol]

    FIRST[symbol] = set()

    if not symbol.isupper():
        FIRST[symbol].add(symbol)
        return FIRST[symbol]

    for production in grammar[symbol]:
        if production == "ε":
            FIRST[symbol].add("ε")
        else:
            i = 0
            while i < len(production):
                if i + 1 < len(production) and production[i + 1] == "'":
                    sym = production[i:i+2]
                    i += 2
                else:
                    sym = production[i]
                    i += 1

                sym_first = first(sym)
                FIRST[symbol].update(sym_first - {"ε"})

                if "ε" not in sym_first:
                    break
            else:
                FIRST[symbol].add("ε")

    return FIRST[symbol]

# Compute FIRST sets
for nt in grammar:
    first(nt)

# ---------------- FOLLOW computation ----------------

FOLLOW = {nt: set() for nt in grammar}

# Start symbol
start_symbol = "E"
FOLLOW[start_symbol].add("$")

def get_symbols(production):
    """Split production into symbols (handles E', T', etc.)"""
    symbols = []
    i = 0
    while i < len(production):
        if i + 1 < len(production) and production[i + 1] == "'":
            symbols.append(production[i:i+2])
            i += 2
        else:
            symbols.append(production[i])
            i += 1
    return symbols

changed = True
while changed:
    changed = False

    for A in grammar:
        for prod in grammar[A]:
            if prod == "ε":
                continue

            symbols = get_symbols(prod)

            for i, B in enumerate(symbols):
                if B not in grammar:
                    continue

                # Case: symbols after B
                beta = symbols[i + 1:]
                if beta:
                    first_beta = set()
                    for sym in beta:
                        sym_first = first(sym)
                        first_beta.update(sym_first - {"ε"})
                        if "ε" not in sym_first:
                            break
                    else:
                        # All symbols in beta can produce ε
                        first_beta.add("ε")

                    before = len(FOLLOW[B])
                    FOLLOW[B].update(first_beta - {"ε"})
                    if "ε" in first_beta:
                        FOLLOW[B].update(FOLLOW[A])
                    if len(FOLLOW[B]) > before:
                        changed = True
                else:
                    # B is at the end
                    before = len(FOLLOW[B])
                    FOLLOW[B].update(FOLLOW[A])
                    if len(FOLLOW[B]) > before:
                        changed = True

# Display FOLLOW sets
print("\nFOLLOW Sets:")
for nt in FOLLOW:
    print(f"FOLLOW({nt}) = {FOLLOW[nt]}")
