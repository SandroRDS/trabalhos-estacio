def selectionSort(arr):
    for selectionIndex in range(len(arr) - 1):
        for comparisonIndex in range(selectionIndex + 1, len(arr)):
            if (arr[comparisonIndex] < arr[selectionIndex]):
                aux = arr[selectionIndex]
                arr[selectionIndex] = arr[comparisonIndex]
                arr[comparisonIndex] = aux


arr = [
    78, 66, 49, 83, 51, 91, 90, 89, 29,
    55, 78, 66, 49, 83, 51
]

selectionSort(arr)

print(arr)