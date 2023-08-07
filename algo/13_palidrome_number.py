# @param {Integer} x
# @return {Boolean}
from helper import Helper


def is_palindrome(x):
    # outliers
    #   if x is negative return false

    # first
    # turn x into a string
    # create 2 pointers for beginning and end
    # loop
    #   if first and last value are equal
    #     continue loop
    #   if not return false
    # if we successfully make it through the loop
    #   return true

    if x < 0:
        return False

    x_str = str(x)

    l, r = 0, len(x_str) - 1

    while l < r:
        if x_str[l] != x_str[r]:
            return False
        l += 1
        r -= 1
    return True


def is_palindrome_int(x):
    # second
    # Math!
    if x < 0:
        return False

    input = x
    new_num = 0

    # Reverse using math
    while x > 0:
        new_num = int(new_num * 10) + (x % 10)
        x = int(x / 10)
        print(f"new: {new_num}, x: {x}")
    return new_num == input


Helper.top_wrap("TESTING...")
print(is_palindrome_int(121))
print(is_palindrome_int(123456789))
print(is_palindrome_int(1234567654321))
print(is_palindrome_int(-121))
print(is_palindrome_int(10))
