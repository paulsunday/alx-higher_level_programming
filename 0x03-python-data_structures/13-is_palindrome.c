#include "lists.h"
#include <stddef.h>
/**
 * is_palidrome- checks if a linked list is a palindrome
 * @head: pointer to the head of the list
 * Return: 1 if palidrome, 0 if not
 */
int is_palindrome(listint_t **head)
{
	int result = 1;
	listint_t *fast, *slow, *h1, *h2, *tmp;
	if (!head)
		return (0);
	/*if list len is less than 2*/
	if (!(*head) || !((*head)->next))
		return (1);
	/* find the middle node */
	slow = fast = *head;
	while (fast && fast->next)
	{
		slow = slow->next;
		fast = fast->next->next;
	}
	if (fast)
		slow = slow->next;
	/* reverse the last half */
	h2 = reverse_listint(&slow);
	tmp = h2;
	
	/* compare the two halves */
	h1 = *head;
	while (h2)
	{
		if (h2->n != h1->n)
		{
			result = 0;
			break;
		}
		h1 = h1->next;
		h2 = h2->next;
	}
	/* reverse the half back to original */
	reverse_listint(&tmp);
	return (result);
}
/**
 * reverse_listint - reverses a linked list
 * @h: head of the list
 * Return: ppointer to the reversed list
 */
listint_t *reverse_listint(listint_t **h)
{
	listint_t *tmp2, *tmp1;
	if (!h || !(*h))
		return (NULL);
	tmp1 = (*h)->next;
	(*h)->next = NULL;
	while (tmp1)
	{
		tmp2 = *h;
		*h = tmp1;
		tmp1 = (*h)->next;
		(*h)->next = tmp2;
	}
	return (*h);
}
