def bubblesort(array):
    n = 1

    while n < len(array):
        for i in  range(len(array)- n):
            if array[i] > array[i+1]:
                array[i], array[i+1] = array[i+1], array[i]

        n += 1

array = [8,1,3,6,7,4,2,5]
bubblesort(array)
print(array)