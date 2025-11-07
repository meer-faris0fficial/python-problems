def multiplication_of_table():
    print("Wellcome to the multiplication of table calculator")
    num = input("Enter the number: ")
    
    try:
        num = int(num)
    except ValueError:
        print("please enter the input as integers")
        return
    if num < 0:
        print("Enter the positive integer")
        return
    
    i = 1
    while ( i <= 10 ):
        ans = num * i
        print(f"{num} X {i} = {ans}")
        i += 1
        
multiplication_of_table()