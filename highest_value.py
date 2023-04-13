def large(arr):

    max = arr[0]

    for i in range(0, len(arr)):
        if arr[i] > max:
            max = arr[i]
    return max

arr = [229,123,3342,862,222]
print("Highest number in the given array is :",large(arr))
