""" 
Bubble sort sorts a list in place. In other words, it does not create a new Array; instead, it modifies the Array that was passed to the function as an argument.

To achieve this in-place sorting, bubble sort swaps elements when they are in the incorrect order. When no swaps occur, the Array is considered sorted. This algorithm iterates over an Array over and over until it is sorted. If the input Array is already sorted, it iterates over it only once because no swaps occur.

Let's look at a step-by-step example with an unsorted list:

Input: [2, 3, 1]
2 is less than 3, so it stays where it is
But 1 is less than 3 so those two values are swapped
Pass 1: [2, 1, 3]

1 is less than 2, so those values are swapped
2 is less than 3, so those values stay as is
Pass 2: [1, 2, 3]

On this final pass, no swaps occur, so Array is sorted
Pass 3: [1, 2, 3]

And here's what happens with a sorted list:
Input: [1, 2, 3]
  No swaps occur when iterating over Array
  Input Array is returned as is
  Pass 1: [1, 2, 3]

"""

from helper import Helper
from random import randint
def bubble_sort(lst):
  # iterate through the arr
	#  compare the current element vs the next element
	#    if the current is bigger
	#      then we swap
	# go through swapping until the array is Fully sorted

  swapped = False
  counter = 0
  for i in range(len(lst) - 1):
    for j in range(len(lst) - i - 1):
      counter +=1
      # Nested loop to compare all pairs
      if lst[j] > lst[j + 1]:
        swapped = True
        lst[j], lst[j + 1] = lst[j + 1], lst[j]
    if not swapped:
      return
    
    
Helper.top_wrap("BUBBLE")

lst1 = [3,2,1]
lst2 = [1,2,3]
lst3 = []

lst_rand = []
for x in range(100):
  lst_rand.append(randint(0,1000))

print(lst1)
print(lst2)
print(lst3)
print(lst_rand)
bubble_sort(lst1)
bubble_sort(lst2)
bubble_sort(lst3)
bubble_sort(lst_rand)
print(lst1)
print(lst2)
print(lst3)
print(lst_rand)
