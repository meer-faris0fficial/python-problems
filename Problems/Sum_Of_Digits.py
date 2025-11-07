def sum_of_digits():
    num = input("Please enter the number: ")
    
    try:
        num = int(num)
    except ValueError:
        print("Invalid input, please enter the number!")
        return   
    
    if num < 0: # if we uses this inside the loop it will never run as if the number is negative then the 
        print("Please enter the positive integer")# loop runs conditions is false and loop terminate
        return # this will terminate the program if no is negative
    
    sum = 0
    while (num > 0):
        sum = sum + (num % 10)
        num  //= 10  # here floor division is used to remove the remaining decimal value of answer(num)
    print(f"sum of digits is: {sum}")
    
sum_of_digits()

