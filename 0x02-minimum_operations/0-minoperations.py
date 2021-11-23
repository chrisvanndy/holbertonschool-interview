#!/usr/bin/python3
"""Create formula to return minimum number operations required to yeild n"""

def minOperations(n):
    """Returns minimum number operations to yeild n
    
    Arguments: n, number of characters to be printed. cp, use of both the copy and paste function. ops, the total number of operations performed.
    
    Returns:  the total number of opertaions required to yield n"""
    
    ops = 0
    cp = 2

    # as the loop runs, n will be divided down the accomodate chars left to print
    while n > 1:
      # if characters left to print is a factor of 2 (copy + paste = 2 actions)
      if (n % cp == 0):
        # add number of actions to operations variable
        ops += cp
        n /= cp
      else:
        # if n is not a factor of 2, paste 1 additional character and try again.
        cp += 1

    return ops

    
 


    
        
    return operations
    



