class DoublyLinkedList():
    pass

    """ 
       A doubly linked list node points to the next and previous node

       node = {value, next, previous}
       head => previous that points to None
       tail => next that points to None


          Big O:
          - Append(add)           O(1)
          - Prepend(remove)       O(1)
          - Traverse              O(N/2) => O(N)
          - Insert                O(N)
          - Delete                O(N)

        This one holds a lot more data
    """