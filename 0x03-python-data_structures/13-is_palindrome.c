#include "lists.h"

/**
 * is_palindrome - checks if a singly linked list
 * is a palindrome
 * @head: pointer to head of list
 * Return: 0 if it is not a palindrome,
 * 1 if it is a palndrome
 */
int is_palindrome(listint_t **head)
{
	int ndata[1024];
	int size, i;
	listint_t *h;

	h = *head;
	size = 0;

	while (h != NULL)
	{
		size++;
		h = h->next;
	}

	h = *head;
	i = 0;

	while (h != NULL)
	{
		ndata[i] = h->n;
		h = h->next;
		i++;
	}

	for (i = 0, size--; i <= size; i++, size--)
	{
		if (ndata[i] != ndata[size])
		{
			return (0);
		}
	}

	return (1);
}
