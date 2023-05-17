def selectionSort(array):

	for i in range(len(array)):
		min = i

		for j in range(i + 1, len(array)):

			if array[j] < array[min]:
				min = j

		(array[i], array[min]) = (array[min], array[i])

arr = [-2, 45, 0, 11, -9,88,-97,-202,747]
selectionSort(arr)
print('The array after sorting in Ascending Order by selection sort is:')
print(arr)
