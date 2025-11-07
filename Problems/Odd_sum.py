# calculate the sum of odd number to the varable user provides

def Odd_sum():
    print("Wellcome to odd sum calculator")
    num = input("Please enter the number: ")
    
    try:
        num = int(num)
    except ValueError:
        print("please enter the input as integers")
        return
    if num < 0:
        print("Enter the positive integer")
        return
    
    sum = 0
    i = 1
    while ( i <= num ):
        sum += i
        i += 2
    print(f"The of the odd numbers till {num} is {sum} ")
    
Odd_sum()