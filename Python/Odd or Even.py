'''
Given an array of numbers (a list in groovy), determine whether the sum of all of the numbers is odd or even.

Give your answer in string format as 'odd' or 'even'.
'''

#my solution
def oddOrEven(arr):
    return "even" if sum(arr) % 2 == 0 else "odd"

#Other solutions 

def oddOrEven(arr):
    return ('even', 'odd')[sum(arr) % 2]

def oddOrEven(arr):
    return {True: 'odd', False: 'even'}[sum(arr)%2]