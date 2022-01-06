#include <stdlib.h>
#include <stdio.h>
#include "palindrome.h"

/**
 * is_palindrome - function determins if int is palindrome
 * based on argv/argc input from the user
 * @n: long unsigned integer
 *
 * Return: 1 if a palindrom, 0 if not a palindrome
 */

int is_palindrome(unsigned long n)
{
    unsigned long rev = 0, num = n;
	int digit;
    /* int i = 0; */

    while (num > 0)
    {
        digit = num % 10;
        /* printf("%d.) %d \n", i, digit); */
        rev = rev * 10 + digit;
        /* printf("%d.) %lu \n", i, rev); */
        num = num / 10;
        /* printf("%d.) %lu \n", i,n); */
        /* i++; */ 
    }
    
    if (n == rev)
        return 1;
    else 
        return 0;
}
