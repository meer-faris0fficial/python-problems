class LCM:
    
    def __init__(self):
        self.num1 = int(input("Enter the first number: "))
        self.num2 = int(input("Enter the second number: "))
        self.result = self.work()
        
    def work(self): 
        i = 1
        while(True):
            factor = self.num1 * i
            if factor % self.num2 == 0:
                return factor
            i +=1

lcm = LCM()
print(f"The LCM of {lcm.num1} and {lcm.num2} is:  {lcm.result}")