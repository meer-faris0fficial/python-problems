class GCD:
    
    def __init__(self):
        print("wellcome to the GCD calculator")
        self.num1 = int(input("Enter the first number:"))
        self.num2 = int(input("Enter the second number:"))
        self.result = self.calculate()
        
    def calculate(self):
        self.gcd = 1
        i = 2
        least = self.least()
        while (i <= least):
            if (self.num1 % i == 0 and self.num2 % i == 0):
                self.gcd = i
            i += 1
        return self.gcd
    
    def least(self):
        if self.num1 < self.num2 :
            return self.num1
        else:
            return self.num2
                
gcd = GCD()
print(f"The gcd of {gcd.num1} and {gcd.num2} is:  {gcd.result}")