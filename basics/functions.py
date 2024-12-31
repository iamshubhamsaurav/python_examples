def sum(n1, n2):
    return n1 + n2

def sub(n1, n2):
    return n1 - n2

def greetSomeone(greeting, name):
    return greeting + " " + name

print(sum(12,13))
print(sub(25,15))
print(greetSomeone("Hello", "Shubham"))

# functions with return types
def returnNothing() -> None:
    print("Just a normal function")

def returnInt(num) -> int:
    return num * num;

returnNothing()
print(returnInt(23))