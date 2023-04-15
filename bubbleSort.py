def bubble(arr):
    n = len(arr)
    swapped = False

    for i in range (n - 1):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                swapped = True
                arr[j],arr[j+1] = arr[j+1], arr[j]
        if not swapped:
            return

arr = [43,46,22,67,65,21,34,7,9]
print("unsorted array")
print(arr)

bubble(arr)
print("Sorted array")
print(arr)
