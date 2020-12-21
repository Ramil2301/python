def merger(left_arr, right_arr):
    sorted_arr = []
    left_arr_index  = 0
    right_arr_index = 0

    left_arr_length  = len(left_arr)
    right_arr_length = len(right_arr)

    for _ in range(left_arr_length + right_arr_length):
        if left_arr_index < left_arr_length and right_arr_index < right_arr_length:

            if left_arr[left_arr_index] <= right_arr[right_arr_index]:
                sorted_arr.append(left_arr[left_arr_index])
                left_arr_index += 1

            else:
                sorted_arr.append(right_arr[right_arr_index])
                right_arr_index += 1

        elif left_arr_index == left_arr_length:
            sorted_arr.append(right_arr[right_arr_index])
            right_arr_index += 1

        elif right_arr_index == right_arr_length:
            sorted_arr.append(left_arr[left_arr_index])
            left_arr_index += 1

    return sorted_arr

def mergesort(array):
    if len(array) <= 1:
        return array

    mid = len(array) // 2

    left_arr = mergesort(array[:mid])
    right_arr = mergesort(array[mid:])

    return merger(left_arr, right_arr)

array = [1,7,2,5,6,4,3]
sorted_array = mergesort(array)
print(sorted_array)