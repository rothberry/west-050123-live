""" 
  1. Rewrite the Problem
    - Remove the duplicates of a sorted array, then return the number of unique elements
    - Remove the dups, the return the length of the new uniq array
    - Define any assumptions
  2. Write your own/get test cases
  3. Pseudocode (Whiteboarding) !!!
    - how to solve the algorithm in code speak without actual code
  4. Code
    - Translating our pseudocode into real working code
    - Trying to get as many Base Case Tests to pass
  5. Make it work! Always make it DRY
    - Pass ALL the tests including any stretch cases
  6. Make it optimal
    - Reduce the time/space coplexity, refactor out functions, reduce variables, etc...
  
"""

""" 
Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once. The relative order of the elements should be kept the same. Then return the number of unique elements in nums.

Consider the number of unique elements of nums to be k, to get accepted, you need to do the following things:

- Change the array nums such that the first k elements of nums contain the unique elements in the order they were present in nums initially. The remaining elements of nums are not important as well as the size of nums.
- Return k.

"""




from ipdb import set_trace
from os import system
def remove_dupilicates(nums):
    # ? First
    # In python
    # Turn the nums into a set()
    # the return the length of the new set
    # uniq_set = set(nums)
    # print(uniq_set)
    # return len(uniq_set)  # O(N)

    # ? Second
    # create a new list with the starting element of the nums list
    #   only able to do this because of the nums.length constraints
    # Iterate through nums
    #   for each num
    #     check if the LAST element in new list is NOT the same
    #       add to the list
    #     If not,
    #       skip
    # return the length of the output list
    # output = [nums[0]]
    # for num in nums:
    #     if output[-1] != num:
    #         output.append(num)
    # print(output)
    # return len(output) # O(n) space: O(n)

    # ? Third
    # iterate over the nums
    #   for each:
    #     check if the NEXT element is equal to the CURRENT element
    #       if so,
    #         remove either the current idx
    #       if not, continue
    # return the length of the new modified nums list

    idx = 0
    while idx < len(nums) - 1:
        current = nums[idx]
        nxt = nums[idx + 1]
        if current == nxt:
            nums.pop(idx)
            # our index won't increase on pop
            print(f"New: {nums}")
        else:
            idx += 1
    print(f'Out: {nums}')
    return len(nums)


nums1 = [1, 1, 2]
sol1_list = [1, 2]
sol1 = 2
nums2 = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
sol2_list = [0, 1, 2, 3, 4]
sol2 = 5
# Stretch cases are the odd inputs that may deviate from the normal solution
nums3 = [1]
sol3 = 1


system("clear")
print("TESTING....")

# sol1 == 2, [1,2]
print(remove_dupilicates(nums1) == sol1)
print(remove_dupilicates(nums2) == sol2)
print(remove_dupilicates(nums3) == sol3)
