#!/usr/bin/python3

"""
0-making_change solution file.
"""

from audioop import reverse


def makeChange(coins, total):
  """Given value of coins, return least amm coins needed to make change"""
  if (total <= 0):
    return 0
  """Sort coins, and reverse list to start with largest amm"""
  sortedcoins = sorted(coins)
  sortedcoins.reverse()
  """Counter variable, total returned coins"""
  coinsreturned = 0

  for coin in sortedcoins:
    """current ammount of change needed modulo largest coin"""
    div = total // coin  
    coinsreturned += div
    """subtract largest product of whole coins which can be returned"""
    total -= (div * coin)
 
  if total != 0:
    return -1

  return coinsreturned
  