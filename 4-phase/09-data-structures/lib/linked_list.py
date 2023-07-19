from node import Node


class LinkedList():
    """ 
          beg         end     head    tail
          q = [_, _, _, _, _]     None    None
          add (1)
          q = [1, _, _, _, _]     1       1
          q = [1 => None]     
          add (2)
          q = [2, 1, _, _, _]     2       1
          q = [2 => 1 => None]    
          add (3)
          q = [3, 2, 1, _, _]     3       1
          q = [3 => 2 => 1 => None]    
          add (4)
          q = [4, 3, 2, 1, _]     4       1
          q = [4 => 3 => 2 => 1 => None]    
          add (5)
          q = [5, 4, 3, 2, 1]     5       1
          q = [5 => 4 => 3 => 2 => 1 => None]    
          remove the next number up
          q = [5, 4, 3, 2, _]     5       2
          q = [5 => 4 => 3 => 2 => None]    
          remove the next number up
          q = [5, 4, 3, _, _]     5       3
          q = [5 => 4 => 3 => None]    
          add (6)
          q = [6, 5, 4, 3, _]     6       3
          q = [6 => 5 => 4 => 3 => None]    

          Pointers!
          - The node that points to the next value in the sequence


          Head => the first
          Tail => the last, or the last value to point to None

          Big O:
          - Append(add)           O(1)
          - Prepend(remove)       O(1)
          - Traverse              O(N)
          - Insert                O(N)
          - Delete                O(N)


    """

    def __init__(self, value):
        self.head = Node(value)
        self.tail = self.head
        self.length = 1

    def append(self, value):
        new_node = Node(value)
        self.tail.next = new_node
        self.tail = new_node
        self.length += 1
        return self

    def prepend(self, value):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node
        self.length += 1
        return self
    
    def traverse(self, index):
        # start from the head, and move .next until the "index"
        current_node = self.head
        i = 0
        while i != index:
            current_node = current_node.next
            i += 1
        return current_node