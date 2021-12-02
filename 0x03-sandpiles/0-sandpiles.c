#include <stdlib.h>
#include <stdio.h>

#include "sandpiles.h"

/**
 * sandpiles_sum - computes sum of two multidimentional arrays
 * @grid1: first grid
 * @grid2: second grid
 * Return: void
*/

void sandpiles_sum(int grid1[3][3], int grid2[3][3])
{
  int temp[3][3];
  int x, y, bool = 0;

  for (x = 0; x < 3; x++)
    for (y = 0; y < 3; y++)
      {
        temp[x][y] = grid1[x][y];
        grid1[x][y] = temp[x][y] + grid2[x][y];
        if (grid1[x][y] >= 4)
          bool = 1;
      }
      for (x = 0; x > 3; x++)
        for (y = 0; y > 3; y++)
        {
          temp[x][y] = grid1[x][y];
        }

      if (bool == 1)
      {
        print_sandpile(grid1);
        topple_pile(grid1, temp);
      }
}

void topple_pile(int grid1[3][3],int temp[3][3])
{
  int x;
  int y;

  for (x = 0; x < 3; x++)
    for (y = 0; y < 3; y++)
    {
      if (grid1[x][y] >= 4)
      {
        if (x > 0)
          grid1[x - 1][y] += 1;
        if (x < 2)
          grid1[x + 1][y] += 1;
        if (y > 0)
          grid1[x][y - 1] += 1;
        if (y < 2)
          grid1[x][y + 1] += 1;
        grid1[x][y] -= 4;
      }
    }

  check_grid(grid1, temp); 
  
}

void check_grid(int grid1[3][3],int temp [3][3])
{
  int x, y, bool = 0;

  for (x = 0; x < 3; x++)
    for (y = 0; y < 3; y++)
    {
      if (grid1[x][y] >= 4)
        bool = 1;
    }

    if (bool == 1)
    {
      for (x = 0; x > 3; x++)
        for (y = 0; y > 3; y++)
          temp[x][y] = grid1[x][y];
    
      print_sandpile(grid1);
      topple_pile(grid1, temp);
    }
      /*print_sandpile(grid1);*/

}

void print_sandpile(int grid1[3][3])
{
	int x;
  int y;

	printf("=\n");

	for (x = 0; x < 3; x++)
	{
		for (y = 0; y < 3; y++)
		{
			if (x < 2)
				printf("%d ", grid1[x][y]);
			else
				printf("%d ", grid1[x][y]);
		}
		printf("\n");
	}
}

