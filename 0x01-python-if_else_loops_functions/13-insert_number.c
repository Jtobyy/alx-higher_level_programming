#include "lists.h"


/**
 * insert_node - Inserts a number into a
 * sorted singly linked list
 * @head: Pointer to the head of the list
 * @number: integer to insert
 *
 * Return: Address of the new node, or NULL
 * if it failed
 **/
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *cur;
	listint_t *new;
	listint_t *temp;

	cur = *head;
	if (cur == NULL)
	{
		cur = malloc(sizeof(*cur));
		cur->n = number;
		cur->next = NULL;
		return (cur);
	}
	while (cur != NULL)
	{
		if (cur->n >= number)
		{
			new = malloc(sizeof(*new));
			if (new == NULL)
				return (NULL);
			new->n = cur->n;
			cur->n = number;
			temp = cur->next;
			cur->next = new;
			new->next = temp;
			return (cur);
		}
		if (cur->next == NULL)
		{
			new = malloc(sizeof(*new));
			if (new == NULL)
				return (NULL);
			new->n = cur->n;
			cur->n = number;
			temp = cur->next;
			cur->next = new;
			new->next = temp;
			return (cur);
		}
		cur = cur->next;
	}
	return (NULL);
}
