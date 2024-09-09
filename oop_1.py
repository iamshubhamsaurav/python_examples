# Method overloading
class Calculator:
    def sum(self, n1, n2):
        return n1 + n2
    
    def sum(self, n1, n2, n3):
        return n1 + n2 + n3
    
calc = Calculator()

print(calc.sum(12,23,34))

