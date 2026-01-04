def safe_divide(numerator, denominator):
    """
    Safely divides two numbers with robust error handling.
    
    Args:
        numerator: The dividend (can be string or numeric)
        denominator: The divisor (can be string or numeric)
    
    Returns:
        str: Result message or error message
    """
    try:
        # Attempt to convert inputs to float
        num = float(numerator)
        denom = float(denominator)
        
        # Attempt division
        result = num / denom
        return f"The result of the division is {result}"
        
    except ValueError:
        # Handles non-numeric input
        return "Error: Please enter numeric values only."
    
    except ZeroDivisionError:
        # Handles division by zero
        return "Error: Cannot divide by zero."