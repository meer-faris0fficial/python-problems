def palindrome_no():
    print("Wellcome to the palindrome no calculator")
    num = input("Please enter the number: ")
    
    try:
        num = int(num)
    except ValueError:
        print("please enter the input as integers")
        return
    
    num1 = num
    
    if num < 0:
        print("Enter the positive integer")
        return
    
    newNum = 0
    while (num > 0):
        digits = num % 10
        newNum = newNum * 10 + digits
        num //= 10
    
    if  newNum == num1:
        print("The number is palindrome")
    elif newNum != num1:
        print("The number is not palindrome")  
    
palindrome_no()