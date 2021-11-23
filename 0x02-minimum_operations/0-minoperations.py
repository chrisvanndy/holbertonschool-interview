#!/usr/bin/python3
"""Create formula to return minimum number operations required to yeild n"""

def minOperations(n):
    """Returns minimum number operations to yeild n

    Arguments:
    n: chars to print
    ops: operations to print chars
    cp: copy paste actions (2)

    Returns:  the total number of opertaions required to yield n"""

    ops = 0
    cp = 2

    # while looping, n divided down the accomodate chars left to print
    while n > 1:
        # if characters left to print is a factor of 2
        if (n % cp == 0):
            # add number of actions to operations variable
            ops += cp
            # half n to account for characters still needed to print
            n /= cp
        else:
          # if n is not a factor of 2, paste 1 try again.
            cp += 1

    return ops