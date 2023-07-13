from ipdb import set_trace
from os import system
from pprint import pp
from helpers import term_wrap, star_line, center_string_stars

# ! BIG O NOTATION

# * TIME COMPLEXITY


class ConstantTime():  # O(1)

    def first_func(self):  # TOTAL OPS => O(6)
        x = 1           # O(1)
        y = 2           # O(1)
        name = "layne"  # O(1)
        z = x + y       # O(1)
        print(name)     # O(1)
        return z        # O(1)

    def with_list(self, lst):  # O(4)
        print(len(lst))  # O(1)
        print(lst[0])   # O(1)
        print(lst[1])   # O(1)
        print(lst[-1])  # O(1)


class LinearTime():

    def first_func(self, lst):  # O(N)
        print(len(lst))     # O(1)
        print("len(lst)")   # O(1)
        print("125")        # O(1)
        print(len(lst))     # O(1)
        for el in lst:
            other = "hi"    # O(N)
            print(el)       # O(N)
            print(other)    # O(N)

    # to calc the big o, we needt o go line by line and add each big o
    # O(1 + 1 + 1 + 1 + n + n + n) => O(4 + 3n)
    # n = 1     => O(4 + 3) => O(7)
    # n = 10    => O(4 + 30) => O(34)
    # n = 100    => O(4 + 300) => O(304)
    # n = 100000000000000000    => O(4 + 300000000000000000) => O(3000000000000000004)
    # n = ♾    => O(1 + 3*♾) => Can drop the CONSTANT
    #   => O(3 * ♾) => Can ALSO DROP THE COEFFICENT of N
    # The resulting Big O is just O(N)

    def parallel(self, lst1):  # O(n=len(lst1))
        x = 1               # O(1)
        y = 2               # O(1)
        z = 3               # O(1)
        for el1 in lst1:
            el1 + x         # O(N)
            el1 + y         # O(N)

        for el2 in lst1:
            el2 - z         # O(N)
            el2 - y         # O(N)
        return z            # O(1)
    # O(3 + n + n + n + n + 1 ) => O(4 + 4n) => O(4n) => O(n)

    def parallel2(self, lst1, lst2):  # n = len(lst1), m = len(lst2)
        x = 1               # O(1)
        y = 2               # O(1)
        z = 3               # O(1)
        for el1 in lst1:
            el1 + x         # O(N)
            el1 + y         # O(N)

        for el2 in lst2:
            el2 - z         # O(M)
            el2 - y         # O(M)
        return z            # O(1)
    # O(3 + n + n + m + m + 1 ) => O(4 + 2n + 2m) => O(2n + 2m) => O(n + m)

    def find_el(self, lst, el):
        for x in lst:
            if x == el:
                print(x)
                return "DONE"
            else:
                print("still searching")


class QuadraticTime():

    def add_each_element(self, lst):  # O(n^2)
        # [1,2,3,4] => [2, 3, 4, 5, 3, ....]
        new_list = []
        for el1 in lst:
            for el2 in lst:
                new_list.append(el1 + el2)  # O(n * n)
        print(len(lst))
        print(len(new_list))

    def print_each_element(self, matrix):  # O(n^2)
        for row in matrix:
            for x in row:
                print(f"{x}", end=" => ")
        print("")

    def show_diff_lists(self, lst1, lst2):  # O(n * m)
        for el1 in lst1:
            for el2 in lst2:
                print(f'{el1} : {el2}')


class ConstantSpace():

    def add_one(self, lst):
        return [x + 1 for x in lst]


class LinearSpace():

    def add_one_linear(self, lst):
        output = []
        for x in lst:
            output.append(x + 1)
        return output


class QuadraticSpace():
    def add_one_quad(self, lst):
        output = []
        for x in lst:
            output.append([x + 1] * len(lst))
        return output


if __name__ == "__main__":
    system("clear")
    term_wrap("Big O Notation")
    constant = ConstantTime()
    linear = LinearTime()
    quadratic = QuadraticTime()
    const_space = ConstantSpace()

    # constant.with_list([1 for _ in range(100)])
    # linear.first_func([1 for _ in range(100)])
    # linear.find_el([1,2,3,4,5], 1)
    # linear.find_el([1,2,3,4,5], 5)
    # quadratic.add_each_element([1, 2, 3, 4])
    # quadratic.add_each_element([1 for _ in range(10000)])
    m1 = [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 1, 2, 3],
        [4, 5, 6, 7]
    ]
    # quadratic.print_each_element(m1)
    # quadratic.show_diff_lists([1, 2, 3], [4, 5, 6, 7])

    print(const_space.add_one([1, 2, 3, 4]))

    set_trace()
    center_string_stars("BYE")
