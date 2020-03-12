def is_palindrome(value: str) -> bool:
    """
    This function determines if a word or phrase is a palindrome

    :param value: A string
    :return: A boolean
    """
    a = value.replace ( " ", "")
    b = a.lower()
  
    return b == b[::-1]