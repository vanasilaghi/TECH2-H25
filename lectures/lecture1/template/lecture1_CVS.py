"""
Part 2, Lecture 1

Implement and test argmax() function that returns the location of a maximum.

Tasks
-----

1.  Implement a function argmax() that takes a sequence of numbers and returns 
    the index (position) the maximum element.

2.  Test the function with the following sequence of numbers:
    [2, 3, -1, 7, 4]

3.  Add error handling if an empty sequence is passed. Test the function with an 
    empty sequence.

4.  Use the notebook lecture1-benchmark.ipynb to benchmark your implementation 
    against NumPy's argmax().
"""
import numpy as np

def argmax(values):
    n=len(values)
    vm= -np.inf
    im=0
    for i in range(n):
        if i>vm:
            vm=values[i]
            im=i
    return im

ls=[2,3,-1,7,4]
v=argmax(ls)
print(f"The index of the maximum value is {v}")