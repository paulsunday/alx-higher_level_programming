#include "lists.h"
#include <stdlib.h>
#include <stdio.h>

/**
 * insert_node - insets a number into a sorted singly linked list
 * @head: pointer to the head of the list
 * @number: number to be inserted into the list
 * Return: pointer to number or NULL if failed
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *first, *second, *newnode;

	first = malloc(sizeof(listint_t));
	second = malloc(sizeof(listint_t));
	newnode = malloc(sizeof(listint_t));

	if (*head == NULL)
		return (NULL);

	first = *head;
	second = *head;
	second = second->next;

	while (first != NULL)
	{
		if (number > first->n && number < second->n)
		{
			newnode->n = number;

			first->next = newnode;
			newnode->next = second;
		}
		else
		{
			first = first->next;
			second = second->next;
		}
	}
	return (newnode);
}
