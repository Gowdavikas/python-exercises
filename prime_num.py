num = int(input("Enter the number to check its prime number or not : "))

if num > 1:
    for i in range(2, num//2):
        if(num % i) == 0:
            print(num, "is not a prime number")
        else:
            print(num, "is a prime number")
        break
