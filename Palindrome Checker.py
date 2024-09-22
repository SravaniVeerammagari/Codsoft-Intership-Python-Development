def is_palindrome(s):
    # Remove any non-alphanumeric characters and convert to lowercase
    string = ''.join(char.lower() for char in s if char.isalnum())
    # Check if the string is equal to its reverse
    return string == string[::-1]

# Example usage
print(is_palindrome("madam"))  # Output: True
print(is_palindrome("racecar"))  # Output: True
print(is_palindrome("hello"))  # Output: False
