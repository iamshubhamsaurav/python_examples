# This file contains examples of all kinds of conditional statement in python

# If elif and else contionals
num = int(input("Enter a number: "))

if num < 10:
    print("Num is less than 10")
elif num == 10:
    print("Num is 10")
else:
    print("Num is more than 10")

# Unlike other languages, Python does not have a switch statement.
# You can use multiple elif to simulate switch or
# You can use match and case to simulate the switch statement

lang = input("Enter your fav langauge: ")

match lang:
    case "Python":
        print("Your favourite language is Python")
    case "Java":
        print("Your favourite language is Java")
    case "Javascript":
        print("Your favourite language is Javascript")
    case "Go":
        print("Your favourite language is Golang")
    case _:
        print("We don't the language you have mentioned")