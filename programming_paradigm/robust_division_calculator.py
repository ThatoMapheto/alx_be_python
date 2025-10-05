def safe_divide(numerator, denominator):
    """
    Safely divide two numbers with error handling for division by zero and non-numeric inputs.

    Args:
        numerator: The numerator as string
        denominator: The denominator as string

    Returns:
        str: Result of division or error message
    """
    try:
        # Convert inputs to floats - this will raise ValueError if non-numeric
        num = float(numerator)
        den = float(denominator)

        # Perform division - this will raise ZeroDivisionError if denominator is 0
        result = num / den
        return f"The result of the division is {result}"

    except ValueError:
        return "Error: Please enter numeric values only."
    except ZeroDivisionError:
        return "Error: Cannot divide by zero."
