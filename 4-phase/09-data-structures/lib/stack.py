class Stack():
    pass
    """ 
      LAST IN FIRST OUT

      Think of a Vertical stack of plates

      Build up the stack and can only see the top plate
          bottom  top         top     bottom
      s = []                  None    None
      add(1)      
      s = [1]                 1       1
      add(2)      
      s = [1, 2]              2       1
      add(3)      
      s = [1, 2, 3]           3       1
      remove the top
      s = [1, 2]              2       1
      remove the top
      s = [1]                 1       1
      remove the top
      s = []                  None    None

        Big O:
        - Search/Lookup     O(N)
        - append(add)       O(1)
        - pop(remove)       O(1)

    """
