import re

def analyze_code(code):
    try:
        compile(code, "<string>", "exec")
        return True, "Code syntax is valid"
    except SyntaxError as e:
        return False, f"Syntax error at line {e.lineno}: {e.msg}"


import re

def refactor_code(code):
    suggestions = []
    refactored = code

    # Rule 1: Replace tabs with 4 spaces
    if "\t" in refactored:
        refactored = refactored.replace("\t", "    ")
        suggestions.append("Replaced tabs with 4 spaces")

    # Rule 2: Remove trailing whitespaces
    lines = refactored.split("\n")
    cleaned_lines = []
    for line in lines:
        cleaned_lines.append(line.rstrip())
    cleaned = "\n".join(cleaned_lines)

    if cleaned != refactored:
        refactored = cleaned
        suggestions.append("Removed trailing whitespaces")

    # Rule 3: Improve spacing around operators (=)
    if "=" in refactored and " = " not in refactored:
        refactored = re.sub(r"\s*=\s*", " = ", refactored)
        suggestions.append("Improved spacing around operators")
        # ---------- SYNTAX CHECK ----------
    is_valid, message = analyze_code(code)
    if not is_valid:
        return code, [message]

    # ---------- REFORMAT LOGIC ----------
    lines = code.split("\n")
    refactored_lines = []
    indent_level = 0

    for line in lines:
        stripped = line.strip()

        # Decrease indent after return/pass/break/continue
        if stripped.startswith(("return", "pass", "break", "continue")):
            indent_level = max(indent_level - 1, 0)

        # Fix operator spacing
        stripped = stripped.replace("=", " = ")
        stripped = stripped.replace("+", " + ")
        stripped = stripped.replace("-", " - ")
        stripped = stripped.replace("*", " * ")
        stripped = stripped.replace("/", " / ")

        # Remove extra spaces
        stripped = " ".join(stripped.split())

        # Apply indentation (4 spaces)
        indented_line = (" " * 4 * indent_level) + stripped
        refactored_lines.append(indented_line)

        # Increase indent after block starters
        if stripped.endswith(":"):
            indent_level += 1

    refactored = "\n".join(refactored_lines)

    # Rule 4: Detect unused variables (basic detection)
    assigned_vars = re.findall(r"(\w+)\s*=", refactored)
    for var in assigned_vars:
        if refactored.count(var) == 1:
            suggestions.append(f"Variable '{var}' might be unused")

    # Rule 5: Fix inconsistent indentation
    fixed_lines = []
    for line in refactored.split("\n"):
        stripped = line.lstrip()
        indent_spaces = len(line) - len(stripped)
        indent_level = indent_spaces // 4
        fixed_lines.append("    " * indent_level + stripped)

    fixed_code = "\n".join(fixed_lines)

    if fixed_code != refactored:
        refactored = fixed_code
        suggestions.append("Fixed inconsistent indentation")

    # Rule 6: Ensure newline at end of file
    if not refactored.endswith("\n"):
        refactored += "\n"
        suggestions.append("Added newline at end of file")

    # Default message if no major issues
    if not suggestions:
        suggestions.append("Code structure looks clean. Minor readability improvements only")

    # Fallback safety
    if not refactored.strip():
        refactored = code
        suggestions.append("No changes needed")

    return refactored, suggestions
