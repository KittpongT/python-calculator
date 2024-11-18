class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        result = 0
        if b >= 0:
            for i in range(b):
                result = self.add(result, a)
        else:
            for i in range(-b):
                result = self.subtract(result, a)
        return result

    def divide(self, a, b):
        result = 0
        negA = False
        negB = False
        if a < 0 : 
            negA = True
            a = self.multiply(a, -1)
        if b < 0 :
            negB = True
            b = self.multiply(b, -1)
        if b == 0 : return "Err"
        elif a == 0 :return 0
        else:
            while a >= b :
                a = self.subtract(a, b)
                result = self.add(result, 1)

        if negA :
            result = self.multiply(result, -1)

        if negB :
            result = self.multiply(result, -1)
        return result
    
    def modulo(self, a, b):
        if a == 0 : return "Err"
        elif a < 0:
            while a < 0:
                a = self.add(a, b)
        else:
            while a >= b:
                a = self.subtract(a, b)
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

