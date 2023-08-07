# @param {Integer} n
# @return {Boolean}
from helper import Helper


def is_happy(n):
    # create a set/obj/hash to track which values we've seen already
    # exit conditions: n is 1 or we've seen this n before
    # loop until false or n > 1
    # for each iteration
    #   create a digits arr
    #   sum the squares of the digits, and check if it's inside the set/obj
    #   if not, add to the set/obj and continue looping
    #   if it's in the hash, return false
    #   if it's 1, return true

    seen = set()

    while n > 1:
        # digit_arr = str(n).split()
        digit_arr = get_digits(n)
        sum_of_squares = sum([d ** 2 for d in digit_arr])
        # print(f'n: {n}\t sum: {sum_of_squares}')
        print(f'n: {n}')
        if n in seen:
            return False
        seen.add(n)
        n = sum_of_squares
    return True


def get_digits(num):
    digits_arr = []
    while num > 0:
        digits_arr.insert(0, num % 10)
        num = int(num / 10)
    return digits_arr


Helper.top_wrap("TESTING...")
print(f"19: {is_happy(19)}")
# n=19
# 1^2+9^2=82
# 8^2+2^2=68
# 36+64=100
# 1+0+0=1 true

print(f"2: {is_happy(2)}")
# n=2
# 2^2=4
# 4^2 = 16
# 1 + 36 = 37
# 9 + 49 = 58
# 25 + 64 = 89
# 64 + 81 = 145
# 1 + 16 + 25 = 42
# 16 + 4 = 20
# 4 + 0 = 4

print(f"5: {is_happy(5)}")
# 5
# 25
# 29
# 4 + 81 = 85
# 64 + 25 = 89


print(f"7: {is_happy(7)}")
# n=7
# 7^2=49
# 16+81=97
# 81+49=130
# 1+9+0=10
# 1 true

print(f"3: {is_happy(3)}")
# n=3
# 3^2=9
# 9^2=81
# 64+1=65
# 36+25=61
# 36+1=37
# 9+49...=56
# 25+36=61 => repeating so sad
