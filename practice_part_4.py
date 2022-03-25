# find the max of three numbers

from ast import arg
from audioop import mul


def max_num(a, b, c):
    max = 0
    if a < 1 or b < 1 or c < 1:
        max = 'please input positive numbers'
    elif a > max:
        max = a
    elif b > max:
        max = b
    elif c > max:
        max = c
    return max


print(max_num(2, 1, 5))
print(max_num(0, 2, 1))
print(max_num(4, 3, 2))

# solution


def max_sol_num(a, b, c):
    return max([a, b, c])


# multiply all the numbers in a list
# referenced solution

def mult_list(list):
    if len(list) == 0:
        return 0
    prod = list[0]
    if len(list) > 1:
        for i in list[1:]:
            if type(i) is int:
                prod = prod * i
            else:
                prod = prod
    return prod


print(mult_list([1, 2, 3, 4]))
print(mult_list([2, 'word', 6]))


# reverse a string

# recursion method


def rev_rec_string(str, i=0):
    # empty string case
    if len(str) == 0:
        return ""
    # base case
    elif i == len(str)-1:
        return str[0]
    else:
        # recursive case
        return str[-1-i] + rev_rec_string(str, i+1)

# built in shortcut method


def rev_string(str):
    return str[::-1]


print(rev_rec_string('recursion reverse'))
print(rev_string('shortcut reverse'))


# calculate the nth number in a Fibbonacci sequence

def fib(n):
    if n < 0:
        print('invalid input')
    elif n == 0:
        return 0
    elif n == 1 or n == 2:
        return 1
    else:
        return fib(n-1) + fib(n-2)


print(fib(4))
print(fib(7))

# check whether a number falls in a given range


def num_within(n, min, max):
    if n <= max and n >= min:
        return True
    else:
        return False


print(num_within(1, 2, 3))
print(num_within(3, 2, 6))

# solution with python shortcut


def sol_num_within(n, min, max):
    return n in range(min, max+1)


print(sol_num_within(2, 3, 5))
print(sol_num_within(4, 3, 6))

# prints out the first n rows of pascals triangle
# used solution as reference


triangle = [[1], [1, 1]]


def pascal(n):

    if n < 1:
        print('invalid input')
    elif n == 1:
        print(triangle[0])
    else:
        row_number = 2
        while len(triangle) < n:
            row = []
            row_prev = triangle[row_number - 1]
            length = len(row_prev)+1
            for i in range(length):
                if i == 0:
                    row.append(1)
                elif i > 0 and i < length-1:
                    row.append(triangle[row_number-1]
                               [i-1]+triangle[row_number-1][i])
                else:
                    row.append(1)
            triangle.append(row)
            row_number += 1
        for row in triangle:
            new_row = ' '.join(str(e) for e in row)
            print(new_row)


pascal(3)
pascal(5)
