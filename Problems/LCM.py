# LCM of two numbers

def LCM():
    print("Wellcome to the LCM calculator")
    num1 = int(input("please enter the first number: "))
    num2 = int(input("please enter the second number: "))
    
    i = 1
    while(True):
        factor = num1 * i
        if factor % num2 == 0:
            print(f"The LCM of {num1} and {num2} is:  {factor}")
            return
        i +=1
LCM()