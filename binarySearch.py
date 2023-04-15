def binarySearch(array, key, low, high):

    while low <= high:
        mid = low + (high - low)//2
        if array[mid] == key:
            return mid
        elif array[mid] < key:
            low = mid + 1
        else:
            high = mid - 1
    return -1

array = [3,9,23,67,88,99]
key = 67
res = binarySearch(array, key, 0, len(array)-1)

if(res == -1):
    print("Element not found")
else:
    print("Element found at index: ", res)
