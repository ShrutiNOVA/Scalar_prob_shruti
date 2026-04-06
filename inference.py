code = ""
print("Input code:")
while True:
    try:
        line = input()
        code += line + "\n"
    except EOFError:
        break

issues = []
suggestions = []

# RULE 1: Assignment instead of comparison
if "if(" in code and "=" in code and "==" not in code:
    issues.append("Assignment used instead of comparison in if condition")
    suggestions.append("Use '==' instead of '='")

# RULE 2: Unused variable
if "currentValue" in code:
    issues.append("Unused variable detected: currentValue")
    suggestions.append("Remove or use the variable")

# RULE 3: Repeated computation
if code.count("* 2") > 1:
    issues.append("Repeated computation detected")
    suggestions.append("Store computed value instead of repeating")

# RULE 4: Nested loops
if code.count("for(") >= 2:
    issues.append("Nested loops detected (possible inefficiency)")
    suggestions.append("Try optimizing nested loops")

# RULE 5: Magic number
if "* 2" in code:
    issues.append("Magic number detected (hardcoded value)")
    suggestions.append("Use a named variable instead of hardcoding")

# OUTPUT
print("\nDetected issues:")
if issues:
    for i in issues:
        print("-", i)
else:
    print("- None")

print("\nSuggestions:")
if suggestions:
    for s in suggestions:
        print("-", s)
else:
    print("- None")

score = max(0, 10 - len(issues)*2)
print(f"\nFinal score: {score}/10")