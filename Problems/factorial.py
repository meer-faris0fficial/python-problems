def factorial():
    print("Wellcome to the factorial calculator")
    num = int(input("Enter the number: "))
    
    if num < 0:
        print("Please enter the positive integer")
        return
    
    if 0 <= num < 2:
        print(f"The factorial of the {num} is: 1")
        return 
    
    fact = 1
    i = 2
    while( i <= num):
        fact *= i
        i += 1
    print(f"The factorial of the {num} is: {fact}")        

factorial()