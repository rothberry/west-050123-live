# Given an input Array, rotate k units clockwise, i.e. shift the values rightward k units.
# Without creating an additional array
# k is an integer that is greater than or equal to 0.
from helper import Helper

# ! First
# Loop k times
#   remove the last value of the array
#   and add that last value to the beginning
# return the original array


def rotate_array(arr, k):  # O(k)
    i = 0
    while i < k:
        arr.insert(0, arr.pop())

        i += 1
    print(i)
    return arr

# ! Second (slightly more efficent)
# We can cut the amount of loops down to at least less than the length of the array
# Get the final rotations of the array by getting the remainder of the k % arr.length
# Loop THAT many times
#   remove the last value of the array
#   and add that last value to the beginning


def rotate_array2(arr, k):  # O(n)
    i = 0
    rotations = k % len(arr)
    while i < rotations:
        last_value = arr.pop()
        arr.insert(0, last_value)
        i += 1
    print(i)
    return arr


Helper.top_wrap("TESTING...")
print(rotate_array2([1, 2, 3, 4], 1))  # [2,3,4,1]
print(rotate_array2([1, 2, 3, 4], 2))  # [3,4,1,2]
print(rotate_array2([1, 2, 3, 4], 3))
print(rotate_array2([1, 2, 3, 4], 4))
print(rotate_array2([1, 2, 3, 4], 101))  # [2,3,4,1]
