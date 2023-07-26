# For this task, you'll need to write a method that reverses a string. Your method will receive one argument, a string, and be expected to output that string with its letters in reverse order.

# Do not call any type of built-in reverse method!
import os

def reverse_string(str):
    # ? First (Looping last => first)
    # Start by creating an output string/array
    # iterate starting from the end of the string counting down
    # For each loop
    #   push into output string/array
    # return the string/array.join
    # * Time => O(N), Space => O(N)

    # ? Second (Looping first => last)
    # Start by creating an output string/array
    # iterate over the string/array of chars
    # For each loop
    #   unshift/or add the current char to the begining of the output str
    # return the output string/array.join
    # * Time => O(N), Space => O(N)

    # ? Third (Swapping in place)
    # create 2 pointers for the first and last indeces
    # loop until the pointers cross
    # for each
    #   swap the values of the chars
    #     May need a temp var to swap depending on the language
    # return the string
    # * Time => O(N), Space => O(1)

    # ? Fourth(Super Python Easy)
    # str.reverse()
    
    pass


str1 = "hi"
str2 = "catbaby"
str3 = "this is cool"
str4 = ""

os.system("clear")
print("testing...")
