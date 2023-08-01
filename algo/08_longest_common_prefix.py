# @param {String[]} strs
# @return {String}
# Write a function to find the longest common prefix string amongst an array of strings.

# If there is no common prefix, return an empty string "".
from helper import Helper


def longest_common_prefix1(strs):
    # ! FIRST
    # create empty output string
    # loop starting at 0
    #   loop through arr
    #     if all elements at that postion are equal
    #       add to output
    #     if not,
    #       end loops
    # return the output string

    out = ""
    first = strs[0]
    i = 0
    while i < len(first):
        j = 1
        while j < len(strs):
            ele = strs[j]
            if first[i] != ele[i]:
                return out
            j += 1
        out += first[i]
        print(out)
        i += 1
    return out

    # ! Second
    # Sort the list first by length of string
    # or find the length of the shortest string
    # then limit the looping to the length
    # Same as above
    

Helper.top_wrap("TESTING....")


strs1 = ["flower", "flow", "flight"]
strs2 = ["dog", "racecar", "car"] 
strs3 = ["ra", "raa", "ra", "ra"]


print(longest_common_prefix1(strs1))
print(longest_common_prefix1(strs2))
print(longest_common_prefix1(strs3))
print(longest_common_prefix1([]))

