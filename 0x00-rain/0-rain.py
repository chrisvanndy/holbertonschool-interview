#!/usr/bin/pmax_comparethon3
"""Determines the amount of cubic rainwater collected within a contained area"""

def rain(walls):

  water = 0

  """Determins total cubic rainfall
  
  Arguments:
    wall: list of integers, representing wall height

  Returns:
    Value for cubic rain fall based on wall heights in list
  """

  if not walls:
    return (0)

  if (len(walls) <= 0):
    return (0)

  for index in range(0, len(walls) -1):
    min_wall = walls[index]
    max_wall = walls[index]
    for max_compare in range(index):
      min_wall = max(min_wall, walls[max_compare])
    for max_compare in range(index + 1, len(walls)):
      max_wall = max(max_wall, walls[max_compare])
    water += min(min_wall, max_wall) - walls[index]
  return (water)


  

