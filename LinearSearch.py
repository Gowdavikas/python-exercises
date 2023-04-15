def LinearSearch(array,key):

    for i in range(0, len(array)):
        if array[i] == key:
            return i
    return -1

array = [23,14,56,32,36,85,24,9]
key = 56
res = LinearSearch(array,key)

if(res == -1):
    print("Element not found")
else:
    print("Element found at index: ", res)
