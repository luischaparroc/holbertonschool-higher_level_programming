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
	listint_t *h1;
	listint_t *h2;
	listint_t *h3;

	if (*head == NULL)
		return (1);

	if ((*head)->next == NULL)
		return (1);

	h1 = h2 = *head;
	h3 = NULL;

	while (h1 != h3)
	{
		while (h2->next != h3)
			h2 = h2->next;

		if (h1->n != h2->n)
			return (0);

		h1 = h1->next;

		if (h1->next == h2)
			return (1);

		h3 = h2;
		h2 = h1;
	}

	return (1);
}
