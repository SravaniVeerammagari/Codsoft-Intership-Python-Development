# String Reversal using slicing operator
# function to reverse a string
def reverse(string):
    # slice syntax for reversed string
    reversed_string = string[::-1]
    return reversed_string
# declaring a string to reverse
string = "cognifyz"
# printing a statement of which method is used
print(f"String Reversal using Slicer Operator")
# printing the original string
print(f"Original String: {string}")
# making a function call inside a print function using an f-string
print(f"Reversed String: {reverse(string)}")


# String Reversal using for loop
# a funtion for reverse string
def reverse_string(string):
    # an empty string storing for reversed string
    reversed_string=""
    # looping through a string
    for char in string:
        # reversing a string
        reversed_string=char + reversed_string
        # returning a reversed string
    return reversed_string
# the string to reverse
string = "hello"
# printing a statement of which method is used
print(f"String Reversal using a for loop")
# printing the original string
print(f"Original String: {string}")
# making a function call inside a print function using an f-string
print(f"Reversed String: {reverse_string(string)}")

