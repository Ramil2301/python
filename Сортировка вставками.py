def insertssort(array):
    for i in range(1, len(array)):
        index = array[i]
        j = i - 1

        while j >= 0 and array[j] > index:
            array[j + 1] = array[j]
            j -= 1

        array[j + 1] = index

array = [7,3,4,1,2,6,8]
insertssort(array)
print(array)