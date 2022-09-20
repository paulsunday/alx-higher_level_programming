/**
 * check_cycle - checks a linked list to determine if there is a cycle
 * @list: pointer to the head of the list
 * Return: 1 if has cycle, 0 if no cycle
 */

#include "lists.h"
#include <stdio.h>

int check_cycle(listint_t *list)
{
	listint_t *fast, *slow;

	if (list == NULL)
	{
		return (0);
	}

	fast = list->next;
	slow = list;

	while (fast != NULL && fast->next != NULL && slow != NULL)
	{
		if (fast == slow)
		{
			return (1);
		}
		fast = fast->next->next;
		slow = slow->next;
	}
	return (0);
}
