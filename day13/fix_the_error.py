# Fix the Errors

age = int(input("How old are you? "))
# just (input("How old are you? ")) => this is return 'string' type. 

if age > 18:
    print(f"You can drive at age {age}.")

# Indentation error have red underline.

# And another problem is "You are getting the input from the console as a string. so you must cast that input string to an 'int' object in order to do numerical operations.