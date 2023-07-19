class MyQueue():
    """ 
        A queue is an ordered list that is First In First Out
        FIFO

        Real World Applications for a queue?
        - Rollercoaster line
        - DMV Line
        - Paperwork if you disregard priority
        - On hold for anything
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
        - Search/Lookup     O(N)
        - Enqueue(add)      O(1)
        - Dequeue(remove)   O(1)


    """


    pass