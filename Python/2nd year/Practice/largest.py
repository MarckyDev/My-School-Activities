def find_largest_and_smallest(arr):
    #sort the array first in ascending order
    smallest = find_smallest(arr)
    largest = find_largest(arr)
    return f"Largest in the array: {largest}\nSmallest in the array: {smallest}"


def find_smallest(arr):
    
    # assume that
    smallest = arr[0]

    for i in range(len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
    
    return smallest

def find_largest(arr):
    
    # assume that
    largest = arr[0]

    for i in range(len(arr)):
        if arr[i] > largest:
            largest = arr[i]
    
    return largest

array = [1, 4, 16, 8, 9, 6, 2, 3] 
print(find_largest_and_smallest(array))
