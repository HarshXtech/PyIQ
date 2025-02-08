def is_leap_year(year: int) -> bool:
    """
    Checks if a given year is a leap year.
    
    Example:
    >>> is_leap_year(2020)
    True
    >>> is_leap_year(2023)
    False
    """
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)
