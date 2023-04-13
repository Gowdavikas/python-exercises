num = int(input("How many terms : "))

n1 = 0
n2 = 1
count = 0

if num < 0:
    print("Number is not-valid, enter positive integer")
else:
    print("The fibonacci sequence of the numbers is: ")
    while count < num:
        print(n1)
        nth = n1 + n2
        n1 = n2
        n2 = nth
        count += 1
