# You are climbing a staircase. It takes n steps to reach the top.

# Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

from helper import Helper
from ipdb import set_trace

"""  
  When you are stuck and don't see the pattern, try manually solving until you see a pattern arise!
  * n = 1 => 1
  1
  * n = 2 => 2
  11
  2
  * n = 3 => 3
  111
  21
  12
  * n = 4 => 5
  1111
  211
  121
  112
  22
  * n = 5 => 8
  1111  1
  211   1
  121   1
  112   1
  22    1
  111   2
  21    2
  12    2
  * n = 6 => 13
  ...
  * n = 7 => 21
  ...
  * n = 8 => 34
  ...
  * n = n => ?
    climbing_stairs(n - 1) + climbing_stairs(n - 2)
    add 1 to the end of all the previous combinations
    add 2 to the end of the n - 2 combiniations

"""

def climbing_stairs(n):
    # create an output list starting with the first 2 results
    # [n=1: 1, n=2: 2]
    # loop n times
    #   inside the loop append the sum of the previous 2 together
    #   OR
    #   move the sum of the 2 to the 2nd and the 2nd value to the first
    # return the last value
    print(f'N => {n}')
    if n < 3:
        return n

    out = [1, 2]
    i = 2
    while i < n:
        out.append(out[i - 1] + out[i - 2])
        # or...
        # out.pop(0)
        # print(out)
        i += 1

    return out[n - 1]



def climbing_stairs_rec(n):
    if n < 3:
        return n
    return climbing_stairs_rec(n - 1) + climbing_stairs_rec(n - 2)


Helper.top_wrap("CLIMBING STAIRS")
print(climbing_stairs(2))
print(climbing_stairs(3))
print(climbing_stairs(4))
print(climbing_stairs(5))
print(climbing_stairs(6))
print(climbing_stairs(7))
print(climbing_stairs(8))
print(climbing_stairs(45))
print(climbing_stairs(46))
print(climbing_stairs(100))
