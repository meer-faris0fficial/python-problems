def prime_number():
    num = input("Please enter the number: ")
    
    try:
        num = int(num)
    except ValueError:
        print("Please enter the vlaue in integers")
        return
    
    if num <= 1:
        print("The number is not prime")
        return
    
    prime = 2
    while (prime < num):
        if num % prime == 0:
            print("The number is not prime")
            return
        prime += 1
        
    print("The number is prime")
      
prime_number()
