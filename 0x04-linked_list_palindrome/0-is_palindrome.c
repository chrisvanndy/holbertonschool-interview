#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * is_palindrome - returns 1 if a linked list is palindrome
 * @head: pointer to list to be freed
 * Return: void
 */

int is_palindrome(listint_t **head)
{
	/*if list is empty return 1 */
	if (!head || !*head)
		return (1);
	
		return (pali_helper(head, *head));
}


/**
* pali_helper - helper function determines if linked list is palindrome
* @left: left most node in list
* @right: right most node in list (reverse comparision via recursion)
* a list is considered a palindrome if empty
* Return: 0 not a palindrome, 1 linked list is a palindrome
*/

int pali_helper(listint_t **left, listint_t *right)
{
	/* empty list is a palindrome */
	if (!right || !*left)
		return (1);
		
	/* recursive method returns 1 if linked list and its reverse */
	/* are in fact a palindrome */
	if (pali_helper(left, right->next) && (*left)->n == right->n)
	{
		/* traverse list */
		*left = (*left)->next;
		/* 	printf("%d\n ^^^ RIGHT\n", right->n); */
		/* is a palindrome if all nodes meet if statement */
		return (1);
	}
	/* not a palindrome */
	else
		return (0);
}
