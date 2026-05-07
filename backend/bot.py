# CodeVisionAI Advanced Bot

import ast

def detect_code_type(code):

    if "def " in code:
        return "Python function"

    elif "class " in code:
        return "Python class"

    elif "for " in code or "while " in code:
        return "Loop structure"

    elif "if " in code:
        return "Conditional statement"

    else:
        return "General code"


def analyze_python_code(code):

    try:
        ast.parse(code)
        return "No syntax errors detected. Your code structure is valid."

    except SyntaxError as e:
        return f"Syntax error detected at line {e.lineno}: {e.msg}"


def suggest_refactor(code):

    suggestions = []

    if len(code) > 200:
        suggestions.append("Consider splitting code into smaller functions.")

    if "==" in code and "True" in code:
        suggestions.append("Avoid using '== True'. Use direct condition instead.")

    if "print(" in code:
        suggestions.append("Consider using logging instead of print for production.")

    if not suggestions:
        return "Your code looks clean. No major refactoring needed."

    return "Refactor suggestions:\n" + "\n".join(suggestions)


def explain_code(code):

    code_type = detect_code_type(code)

    return f"This appears to be a {code_type}. It performs specific operations based on its logic."


def general_programming_response(message):

    msg = message.lower()

    # Greeting
    if any(word in msg for word in ["hello", "hi", "hey"]):
        return "Hello! I'm CodeVisionAI. I can analyze, explain, and refactor your code."

    # WHY questions
    elif "why" in msg:
        return "Changes are usually made to improve code readability, fix bugs, improve performance, or follow best practices."

    # WHAT questions
    elif "what" in msg:
        return "Please provide more details or paste your code so I can explain it clearly."

    # HOW questions
    elif "how" in msg:
        return "Please paste your code or explain your problem, and I will guide you step by step."

    # Refactor
    elif "refactor" in msg:
        return "Refactoring improves readability, structure, and maintainability without changing functionality."

    # Error
    elif "error" in msg or "bug" in msg:
        return "Paste your code and I will help identify and fix the error."

    # Explain
    elif "explain" in msg:
        return "Paste your code and I will explain it clearly."

    # Default intelligent reply
    else:
        return f"I understand your question: '{message}'. Please provide more details or paste your code."


def is_code(message):

    code_indicators = ["def ", "class ", "print(", "if ", "for ", "while ", "{", "}", ";"]

    return any(indicator in message for indicator in code_indicators)


def get_bot_response(user_message):

    msg = user_message.lower()

    # If user pasted code
    if is_code(user_message):

        syntax = check_syntax(user_message)

        explanation = explain_code(user_message)

        return f"""
Brief Explanation of your code:

{explanation}

Syntax Check:
{syntax}

Summary:
This code executes specific logic based on its structure. It defines operations, processes data, and returns results accordingly.
"""

    # If user asks HOW something works
    elif "how" in msg:

        return (
            "Explanation:\n"
            "Code works by executing instructions step by step.\n"
            "Each line performs a specific operation such as creating variables, "
            "running conditions, looping, or returning results.\n\n"
            "For example:\n"
            "• Functions perform tasks\n"
            "• Loops repeat actions\n"
            "• Conditions make decisions\n"
            "• Variables store values\n\n"
            "This helps the program solve problems efficiently."
        )

    # If user asks WHY
    elif "why" in msg:

        return (
            "Explanation:\n"
            "Changes or logic are used to improve performance, readability, "
            "and correctness. This ensures the program runs efficiently and is easier to maintain."
        )

    # If user asks WHAT
    elif "what" in msg:

        return (
            "Explanation:\n"
            "Programming logic consists of instructions executed step by step.\n"
            "These instructions help the computer perform tasks and produce output."
        )

    # Default reply
    else:

        return (
            f"Explanation:\n"
            f"Your question '{user_message}' relates to programming logic.\n"
            f"The system processes instructions, performs operations, and produces output based on the code structure."
        )
