from ipdb import set_trace
from os import system
from pprint import pp
from helpers import term_wrap, star_line, center_string_stars
from my_queue import MyQueue
from linked_list import LinkedList
from stack import Stack
from doubly_linked_list import DoublyLinkedList

""" 
    Datatypes in JS
        - Undefined / boolean / array / number / object / string / null
    
    Datatypes in Python 
        - String 
        - List / Tuple /  Set
        - Dict
        - Boolean
        - Int / Float / BigInt / BigFloat

    When we are talking about data structures, we are mostly focused on the quantity of data, so we are using the lists/arrays/objects/dicts

    Objects/Dicts fall into the datastructure of the Hash(Table)
    - These are the Key/Value DS

    These following DS fall into the list/array
    - Queue
    - Stack
    - Linked List
    - Doubly Linked List

    - Binary Search (Tree)
    ~ Trees

"""


if __name__ == "__main__":
    system("clear")
    term_wrap("DATA STRUCTURES")

    linked = LinkedList(1)
    linked.append(2)
    linked.append(3)
    linked.append(4)
    linked.append(8)
    linked.prepend(1251)
    linked.traverse(3)

    set_trace()
    center_string_stars("BYE")
