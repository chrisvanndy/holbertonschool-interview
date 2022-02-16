#include "menger.h"

/**
 * menger - function prints menger sponge at N^3 level
 *
 * @level - level to extract center of cube
 *
 * Return: void
 */
void menger(int level)
{
	int a = 0, b = 0, c = 0;
	bool printchar = true;

	if (level < 0)
		return;

	if (level == 0)
		printf("#\n");


	for (a = 0; a < pow(3, level); ++a)
	{

		for (b = 0; b < pow(3, level); ++b)
		{

			printchar = true;
			for (c = 0; c < level; ++c)
			{

				if ((a / (int)pow(3, c)) % 3 == 1 && (b / (int)pow(3, c)) % 3 == 1)
					printchar = false;
			}

				if (printchar)
					printf("#");
				else
					printf(" ");

		}

		printf("\n");

	}

}
