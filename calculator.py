class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        sub = True
        if (a < 0 and b > 0) or (a > 0 and b < 0):
            sub = False

        # a, b = abs(a), abs(b)
        if a < 0:
            a = 0 - a
        if b < 0:
            b = 0 - b

        result = 0
        for i in range(b):
            result = self.add(result, a)

        if (sub == False):
            return -result
        return result

    def divide(self, a, b):
        if (b == 0):
            raise ValueError("Cannot divide by zero")

        sub  = True
        if (a < 0 and b > 0) or (a > 0 and b < 0):
            sub = False

        # a, b = abs(a), abs(b)
        if a < 0:
            a = 0 - a
        if b < 0:
            b = 0 - b

        result = 0
        while a >= b:
            a = self.subtract(a, b)
            result += 1

        if (sub == False):
            return -result
        return result
    
    def modulo(self, a, b):
        if (b == 0):
            raise ValueError("Cannot modulo by zero")

        sub = True
        if (a < 0 and b > 0) or (a < 0 and b < 0):
            sub = False

        # a, b = abs(a), abs(b)
        if a < 0:
            a = 0 - a
        if b < 0:
            b = 0 - b
            
        while a >= b:
            a = self.subtract(a, b)
        
        if (sub == False):
            return -a
        return a

# Example usage:
if __name__ == "__main__":
    calc = Calculator()
    print("This is a simple calculator class!")
    print("Example: addition: ", calc.add(1, 2))
    print("Example: subtraction: ", calc.subtract(4, 2))
    print("Example: multiplication: ", calc.multiply(2, 3))
    print("Example: division: ", calc.divide(10, 2))
    print("Example: modulo: ", calc.modulo(10, 3))