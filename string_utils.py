# string_utils.py

def is_palindrome(s: str) -> bool:
    """
    Checks if a given string is a palindrome.
    A palindrome is a word that reads the same forward and backward.
    
    Example:
    >>> is_palindrome("madam")
    True
    >>> is_palindrome("hello")
    False
    """
    return s == s[::-1]
