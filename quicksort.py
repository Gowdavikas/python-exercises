def partition(array, low, high):

	pivot = array[high]
	i = low - 1

	for j in range(low, high):
		if array[j] <= pivot:
			i = i + 1
			(array[i], array[j]) = (array[j], array[i])
	(array[i + 1], array[high]) = (array[high], array[i + 1])
	return i + 1


def quickSort(array, low, high):
	if low < high:
		p = partition(array, low, high)
		quickSort(array, low, p - 1)
		quickSort(array, p + 1, high)

arr = [1, 7, 4, 1, 10, 9, -2]
print("Unsorted Array")
print(arr)

quick(arr, 0, len(arr)-1)

print('Sorted Array in Ascending Order:')
print(arr)
