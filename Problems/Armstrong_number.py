class Armstrong:
    
    def __init__(self):
        print("Wellcome to the armstrong no finder")
        self.num = int(input("Please enter the number: "))
        if self.is_armstrong():
            print("Your number is an armstrong number")
        else:
            print("Your number is not an armstrong number")
    
    def is_armstrong(self):
        numOfDigits = self.no_of_digits(self.num)
        numCopy = self.num
        final_number = 0
        temp = self.num
        while temp > 0:
            last_digit = temp % 10
            temp //= 10
            final_number += self.power(last_digit, numOfDigits)
            
        return final_number == numCopy
    
    def power(self, base, exp):
        result = 1
        i = 0
        while i < exp:
            result *= base
            i += 1
        return result
    
    def no_of_digits(self, n):
        digits = 0
        while (n > 0):
            digits += 1
            n //= 10
        return digits
    
    def __str__(self):   # <-- so print(arms) shows something useful
        return f"Armstrong checker for number {self.num}"
    
arms = Armstrong()
print(arms)