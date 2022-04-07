#!/usr/bin/python3
"""Module containts the rotate_2d_matrix() function"""

def rotate_2d_matrix(matrix):
  """Transposes and reverses a 2D matrix of size n x n"""
  """Rotates the matrix 90 degrees in the clockwise direction"""

  # Transpose matrix rows and columns 
  # define matrix row length for iteration
  for row in range(len(matrix)):
    # define matrix height length for iteration
    for height in range(row, len(matrix)):
      matrix[row][height], matrix[height][row] = matrix[height][row], matrix[row][height]
  
  # Reverse transposed matrix 
  for row in range(len(matrix)):
    matrix[row].reverse()
