""" 
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

"""

from ipdb import set_trace
from os import system


def two_sum_brute(nums, target):
    # ? First
    # BRUTE FORCE
    # check EVERY PAIR FOR THE TARGET
    # 2 + 7 => 9
    # 2 + 11 => 13
    # 2 + 15 => 17
    # 7 + 11 => 18
    # ...
    # then return the indeces for the first matching pair
    # usually will have the highest time and space complexity

    # create an empty list
    # starter index for the left
    # iterate for the length of nums
    #   for each loop
    #     define a second index as i + 1
    #       loop from second index to end of nums
    #         add both indeces and sum to our output
    # after populating the output array
    # iterate over the output array
    #   check if the sum equals the target
    #     return the indeces of that sum

    output, i, = [], 0

    while i < len(nums):
        j = i + 1
        while j < len(nums):
            left, right = nums[i], nums[j]
            sum_lr = left + right
            print(f'left: {left}, right: {right}, sum: {sum_lr}')

            output.append([i, j, sum_lr])
            j += 1
        i += 1

    for x in output:
        if x[2] == target:
            return x[:2]


def two_sum(nums, target):

    # ? Second
    # if we take the difference between the current element and the target, we get a GOAL to search for in the list

    # iterate nums
    # for each element
    #   store the difference between the current and the target
    #   check if we've already seen this value
    #     if so, return the current and goal indeces

    output = {}
    i = 0
    while i < len(nums):
        current = nums[i]
        goal = target - current
        try:
            return [output[current], i]
        except KeyError:
            output[goal] = i
            i += 1
        print(f'cur: {current}, goal: {goal}, output: {output}')


nums1 = [2, 7, 11, 15]
target1 = 26
out1 = [2, 3]
nums2 = [3, 2, 4]
target2 = 6
out2 = [1, 2]
nums3 = [3, 3]
target3 = 6
out3 = [0, 1]

system("clear")
print("TESTING....")

# sol1 == 2, [1,2]
sol1 = two_sum(nums1, target1)
# sol2 = two_sum(nums2, target2)
# sol3 = two_sum(nums3, target3)

print(sol1, sol1 == out1)
# print(sol2, sol2 == out2)
# print(sol3, sol3 == out3)
