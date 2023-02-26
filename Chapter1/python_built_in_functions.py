import time
import timeit
from datetime import datetime
from itertools import permutations
from joblib import Parallel, delayed
import multiprocessing
"""

Chapter 1:
Python Built in Function

"""

'''
Function

Sometimes you might not know the arguments you will pass to a function.
If so, use **kwargs.
**kwargs allow you to pass multiple arguments to a function using a dictionary.
In the exemple below, passing **{'a':1, 'b':2} to the function is similar
to passing a=1, b=1 to the function.
'''

# parameters = {'a':4, 'b':7}
#
# def example(c, **kwargs):
#     print(kwargs)
#     for val in kwargs.values():
#         print("c + val =", c + val)
#
# example(3, **parameters)
#
# print('############################################################################')

'''

Decorator in python

Do you want to add the same block of code to different functions in Python.
If so, try decorator.

In the code below, I created the decorator to track the time of the function say_hello

'''

# (import time )

def time_function(func):
    def wrapper():
        print("This happens before the function is called")
        start = time.time()
        print(start)
        func()
        print("This happens after the function is called")
        end = time.time()
        print(end)
        print("The duration is", end - start, 's')

    return wrapper

# Now all I need to do is to add @time_function before the function say_hello.

# @time_function
# def say_hello():
#     print("Hello")
#
# say_hello()
#
# @time_function
# def func2():
#     pass
# func2()

"""
Code Speed

This section will show you some ways to speed up or track the performance of your Python code.

"""

'''
Concurrently Execute tasks on Sepaarate CPUs

if you ant to execute tasks on separate CPUs to run faster,
consider using jpblib.Parallel. 
It allows you to easily execute several tasks at once, 
wich each task using its own processor

from joblib import Parallel, delayed
import multiprocessing
'''

# def add_three(num: int):
#     return num + 3
#
# num_cores = multiprocessing.cpu_count()
# print("num_cores:", num_cores)
# results = Parallel(n_jobs=num_cores)(delayed(add_three)(i) for i in range(10))
# print("results:", results)

'''
Compare The Execution Time Between 2 Functions

If you want to compare the execution time between 2 functions, try timeit.timeit. 
You can also specify the number of times you want to rerun your function 
to get a better estimation of the time.

import time 
import timeit 
'''

# def func():
#     """comprehension"""
#     l = [i for i in range(10_000)]
#
# def func1():
#     """for"""
#     l = []
#     for i in range(10_000):
#         l.append(i)
#     return l
#
# def func2():
#     """list range"""
#     l = list(range(10_000))
#
# expSize = 1000
# time0 = timeit.timeit(func, number=expSize)
# time1 = timeit.timeit(func1, number=expSize)
# time2 = timeit.timeit(func2, number=expSize)
#
# print("time0: ", time0, '-', "time1: ", time1, '-', 'time2: ', time2, '-', 'time0/time2:', time0/time2, '-', 'time1/time2:', time1/time2)

"""
------------------------------------------------
                    string
------------------------------------------------
"""

'''
Control the Number of Printed Decimals with f-Strings

If you want to limit the number of decimals being printed, use f-string as shown below.
'''

num = 3.3123

print(f'num: 1f: {num: .1f}')   # limit to 1 decimal
print(f'num: 2f: {num: .2f}')   # limit to 2 decimals

'''
Format dates in Python f-Strings

When printing a Python string, f-strings allow you to format datetime easily with a curly bracket and its format.

find all format there: https://docs.python.org/2/library/datetime.html#strftime-and-strptime-behavior

from datetime import datetime
'''

# date = datetime(2023, 2, 26, 17, 2, 45)
date = datetime.now()
print('You need to be there at' f' {date:%I:%M %p} on {date:%A}') # You need to be there at 05:02 PM on Sunday

'''
Pad a String With Zero Using f-String

if you want to pad a string with zero, use f-String
'''

# for hour in range(8, 12):
#     print(f'It is {hour:02} AM, Wake up!')

'''
Use Calculation in Python f-String

if you want to do calculations inside a Pytho string, use f-string.
'''

# apple = 3
# banana = 2
# print(f'The total price is {apple + banana}.')

'''
Debug Your Python Code with an Equal Sign in an f-String

It is common to use f"var={var}" to see which values are being printed.

from itertools import permutations
'''

# nums = [1, 2, 3]
#
# for i,j in permutations(nums, 2):
#     # print(f'i={i}, j={j}')
#     print(f"{i=}, {j=}")

'''
String find: Find The Index of a Substring in a Python String

If you want to find the index of a substring in a string, use find() method. 
This method will return the index of the first occurrence of the substring if found and return -1 otherwise.
'''

sentence = "Today is Saturday"

# Find the index of first occurrence of the substring
sentence.find("day")