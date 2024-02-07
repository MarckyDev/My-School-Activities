'''
You are given a list of n numbers, where n is a power of 2. 
You need to find the two largest numbers in the list. 
Design an algorithm using the Divide and Conquer approach that has a time 
complexity of O(n log n) and explain why it has this time complexity.
'''
import random

def merge_sort(arr):
    if len(arr) > 1:
        # cut in half
        middle = len(arr) // 2
        left_arr = arr[:middle]
        right_arr = arr[middle:]

        
        merge_sort(left_arr)
        merge_sort(right_arr)
        
        counter_left, counter_right, counter = 0, 0, 0
        # sorts the array first
        while counter_left < len(left_arr) and counter_right < len(right_arr):
            if left_arr[counter_left] < right_arr[counter_right]:
                arr[counter] = left_arr[counter_left]
                counter_left += 1
            else:
                arr[counter] = right_arr[counter_right]
                counter_right += 1
                
            counter += 1


        # check if the left and right counter is still within their respective arrays
        # this is merging
        while counter_left < len(left_arr):
            arr[counter] = left_arr[counter_left]
            counter_left += 1
            counter += 1

        while counter_right < len(right_arr):
            arr[counter] = right_arr[counter_right]
            counter_right += 1
            counter += 1

        # returns the last two indexes of the array
        return f"Sorted array: {arr}\nLargest in the array: {arr[-1]}\nSecond largest in the array: {arr[-2]}"

length_of_array = int(input("Please input a number for the length of the array: "))

if length_of_array % 2 == 0:
    array = random.sample(range(0, 100), length_of_array)
    print(merge_sort(array))
else:
    print("The lenght you input is not divisible by 2")