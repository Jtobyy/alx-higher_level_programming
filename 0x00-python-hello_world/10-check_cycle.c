#include "lists.h"


/**
 * check_cycle - Checks if a singly linked list
 * has a cycle in it.
 * @list: pointer to head of list
 * Return: 0 if there is no cycle. 1 if there is a cycle
*/
int check_cycle(listint_t *list)
{
	int counter;
	int i;
	size_t *arr;
	size_t *temp_arr;

	if (list == NULL || list->next == NULL)
		return (0);
	arr = malloc(sizeof(*arr) * 3);
	arr[0] = (size_t)&(list);
	arr[1] = (size_t)&(list->next);
	list = list->next->next;
	counter = 2;
	while (list != NULL)
	{
		for (i = 0; i < counter - 1; i++)
		{
			if ((size_t)&(list->n) == arr[i])
			{
				free(arr);
				return (1);
			}
		}
		arr[counter] = (size_t)&(list->n);
		list = list->next;
		counter++;
		temp_arr = malloc(sizeof(*temp_arr) * counter);
		for (i = 0; i < counter; i++)
		{
			temp_arr[i] = arr[i];
		}
		free(arr);
		arr = malloc(sizeof(*arr) * (counter + 1));
		for (i = 0; i < counter; i++)
		{
			arr[i] = temp_arr[i];
		}
		free(temp_arr);
	}
	free(arr);
	return (0);
}
