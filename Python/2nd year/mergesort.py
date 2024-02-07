def MergeSort(array):
    divide_arr = len(array) // 2

    left_slice = array[divide_arr:]
    right_slice = array[:divide_arr]
    
    MergeSort(left_slice)
    MergeSort(right_slice)
    
    # pointers
    left_pointer, right_pointer, pointer = 0, 0, 0

    while left_pointer < len(left_slice) and right_pointer < len(right_slice):
        if left_slice[left_pointer] < right_slice[right_pointer]:
            array[pointer] = left_slice[left_pointer]
            left_pointer += 1
        else:
            array[pointer] = right_slice[right_pointer]
            right_pointer += 1
        pointer += 1
    
    while left_pointer < len(left_slice):
        array[pointer] = left_slice[left_pointer]
        left_pointer += 1
        pointer += 1


    while right_pointer < len(right_slice):
        array[pointer] = right_slice[right_pointer]
        right_pointer += 1
        pointer += 1

    
    #print('Left Slice: ', left_slice)
    #print('RIght Slice: ', right_slice)
    return array

def merge():
    pass


array = [0, 8, 7, 6, 3, 4, 2 , 9, 1, 10, 11]
print('Before: ', array)
print('After', MergeSort(array))