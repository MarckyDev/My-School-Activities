'''
You are given a list of n integers, and you need to find all pairs of integers 
that sum up to a given target value k. 
Design an algorithm using a hash table that solves this problem in O(n)
time complexity and O(n) space complexity.
'''

def hash_Table(arr, num):
    values = {}
    pair = []

    for numbers in arr:
        if num - numbers in values:
            print('values: ', values)
            print('pairs: ', pair)
            pair.append((numbers, num - numbers))
        values[num] = True
    
    return pair


arr = [1, 2, 3, 4, 5, 6, 6, 8, 9, 10]

num = 6

print(hash_Table(arr, num))