def get_pivot(array, i, j):
	pivot = array[j]
	item = i - 1

	for k in range(i, j):
		if array[k] <= pivot:
			item = item + 1
			(array[item], array[k]) = (array[k], array[item])

	array[item + 1], array[j] = array[j], array[item + 1]

	return item + 1


def quick_sort(array, i=None, j=None):
    if i == None:
        i = 1
    if j == None:
        j = len(array) - 1
        
    if i < j:
        pivot = get_pivot(array, i, j)
        quick_sort(array, i, pivot - 1)
        quick_sort(array, pivot + 1, j)

def bubble_sort(array):
    swapped = True
    while swapped:
        swapped = False

        for i in range(len(array) - 1):
            if array[i] > array[i+1]:
                swapped = True
                aux = array[i]
                array[i] = array[i+1]
                array[i+1] = aux

def selection_sort(array):
    for i in range(len(array)):
        m = i
        for j in range(i+1, len(array)):
            if array[m] > array[j]:
                m = j
        aux = array[i]
        array[i] = array[m]
        array[m] = aux
