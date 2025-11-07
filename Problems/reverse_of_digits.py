def reverse_of_digits():
    num = int(input("Enter the number: "))
    
    newNum = 0
    while (num > 0):
        digits = num % 10
        newNum = (newNum * 10) + digits
        num //= 10
    print(f"the reverse of the number is: {newNum}")
reverse_of_digits()

