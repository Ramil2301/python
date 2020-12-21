def selectionsort(array):
    for i in range(len(array)):
        smallest_value_index = i

        for j in range(i + 1, len(array)):
            if array[j] < array[smallest_value_index]:
                smallest_value_index = j

        array[i], array[smallest_value_index] = array[smallest_value_index], array[i]


array = [2,7,5,3,6,9,4,1]
selectionsort(array)
print(array)