array = [2,4,23,34,57,13,27,20]

for number in array:
    if number % 2 == 0:
        print("Even numbers are :", number)
    elif number % 2 != 0:
        print("Odd numbers are :", number)
    else:
        print("Invalid numbers")