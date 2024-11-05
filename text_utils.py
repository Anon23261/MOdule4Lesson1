# Task: Custom string manipulation functions
def reverse_string(s):
    return s[::-1]

def capitalize_string(s):
    return s.capitalize()

# Main.py
# Task: Import text_utils with an alias and utilize its functions
import text_utils as tu

string = input("Enter a string: ")
print("Reversed string:", tu.reverse_string(string))
print("Capitalized string:", tu.capitalize_string(string))
