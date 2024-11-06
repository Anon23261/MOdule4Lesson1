import mood_responses

mood = input("How are you feeling today? ")
print(mood_responses.mood_response(mood))

import text_utils as tu

string = input("Enter a string: ")
print("Reversed string:", tu.reverse_string(string))
print("Capitalized string:", tu.capitalize_string(string))
