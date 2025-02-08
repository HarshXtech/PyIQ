def is_odd_even(n: int) -> str:
    """
    Determines if a number is odd or even.
    
    Example:
    >>> is_odd_even(4)
    'Even'
    >>> is_odd_even(7)
    'Odd'
    """
    return "Even" if n % 2 == 0 else "Odd"
