# Debug Fizz Buzz Exercise

# When the number is divisible by 3 then instead of printing the number it should print "Fizz". and divisible by 5, then instead of printing the number it should print "Buzz". 

# This is if the number is divisible by both 3 and 5 e.g. 15 then instead of the number it should print "FizzBuzz".

for number in range(1, 101):
    if number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz")
    elif number % 3 == 0:
        print("Fizz")
    elif number % 5 == 0:
        print("Buzz")
    else:
        print(number)

# This code is debugging code. 

# for number in range(1, 5):
#     if number % 3 == 0 or number % 5 == 0:
#         print("FizzBuzz")
#     if number % 3 == 0:
#         print("Fizz")
#     if number % 5 == 0:
#         print("Buzz")
#     else:
#         print([number])



