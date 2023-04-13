def smallest(arr):
    max = 100000

    First  = max
    Second = max
    Third = max

    for i in range (0, len(arr)):
        if arr[i] < First:
            Third = Second
            Second = First
            First = arr[i]
        elif arr[i] < Second:
            Third = Second
            Second = arr[i]
        elif arr[i] < Third:
            Third = arr[i]

    print("The First lowest value is : ", First)
    print("The Second lowest value is : ", Second)
    print("The Third lowest value is : ", Third)

arr = [25, 432, 13, 3, 111, 43, 29]
smallest(arr)
