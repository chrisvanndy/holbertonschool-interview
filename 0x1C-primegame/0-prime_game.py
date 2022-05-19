#!/usr/bin/python3
""" Let's play a 'Prime' Game"""

def allPrimes(x):
    """Returns list of prime numbers up to given parameter, in ascending order.
    Args:
        x (int): list of primes.
    Return:
        primesList (list) of (int): list of primes up to given x, or
        (None): upon fail.
    """

    if (type(x) is not int or x < 0):
        return None

    # logically primes should be a set, but we want it to remain ordered
    primesList = []
    for primeN in range(2, x + 1):
        prime = True
        for divider in range(2, primeN):
            if (primeN % divider == 0):
                prime = False
                break
        if (prime):
            primesList.append(primeN)
    return primesList

def isWinner(n, numbers):
  """
    Returns the winner of a game of 'Primes' between Ben and Maria.

    Players select a prime number from a set of consecutive integers from 1 - 1000. Players remove a prime number (and its multiples) from the given list.
    If a player cannot make a selection, they lose.

    Args:
        n (int): number of rounds.
        numbers (list) of (int): array of x values for each round of the game.
    Return:
        (str): name of the player that won the most rounds (Ben or Maria), or
        (None): on failure or if no winner can be determined.
  """

  if (type(numbers) is not list or not all([type(x) is int for x in numbers]) or
            not all([x > -1 for x in numbers])):
      return None

  if (type(n) is not int or n != len(numbers)):
      return None
  
  numbers.sort()
  primes = allPrimes(numbers[-1])
  if (primes is None):
      return None

  MariaScore = 0
  BenScore = 0
  for x in numbers:
      primeCounter = 0
      for prime in primes:
          if (prime <= x):
              primeCounter += 1
          else:
              break
      if primeCounter % 2 == 0:
          BenScore += 1
      else:
          MariaScore += 1

  if (MariaScore > BenScore):
      return "Maria"
  elif (BenScore > MariaScore):
      return "Ben"
  else:
      return None
