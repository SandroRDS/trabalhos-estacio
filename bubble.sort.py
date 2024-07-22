def bubbleSort(arr):
    for lap in range(len(arr) - 1):
        for index in range(0, len(arr) - lap -  1):
            if (arr[index + 1] < arr[index]):
                aux = arr[index]
                arr[index] = arr[index + 1]
                arr[index + 1] = aux

# arr = [
#     78, 66, 49, 83, 51, 91, 90, 89, 29,
#     55, 78, 66, 49, 83, 51
# ]

# bubbleSort(arr)

# print(arr)