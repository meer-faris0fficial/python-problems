def fibonacci():
    print("Wellcome to the fibonacci series")
    num = int(input("Please enter the number: "))
    
    if num < 0:
        return
    print("0", end=" ")
    if num == 0:
        return
    print("1", end=" ")
    
    first = 0
    second = 1
    while(first + second <= num ):
        third = first + second
        print( third, end=" ")
        first = second
        second = third

fibonacci()