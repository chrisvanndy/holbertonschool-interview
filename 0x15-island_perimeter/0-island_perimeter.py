#!/usr/bin/python3
""" Python Module for evaulating 2d-array"""

def island_perimeter(grid):
  """
      Counts border in a 0, 1 matrix returns the perimeter of an island

  """

  land = 0

  # look at each row 
  for rows in range(len(grid)):
    # look at each column 
    for cols in range(len(grid[0])):
      if grid[rows][cols] == 1:
        # check 1 index neighbors to add to land
        if rows == 0 or grid[rows - 1][cols] == 0:
          land += 1
        if rows == len(grid) - 1 or grid[rows + 1 ][cols] == 0:
          land += 1
        if cols == 0 or grid[rows][cols - 1] == 0:
          land += 1
        if cols == len(grid[0]) - 1 or grid[rows][cols + 1] == 0:
          land += 1

  return land


