number = [44,7,10,27,9,78,99,63,57]
print("Unsorted array : ", number)

i = 0
swapped = True
while swapped:
    swapped = False

    for j in range(len(number)-i-1):
        if number[j] > number[j+1]:
            number[j], number[j+1] = number[j+1], number[j]

print("Sorted   array : ", number)
