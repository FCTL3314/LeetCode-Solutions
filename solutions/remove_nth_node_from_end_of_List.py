# Problem: 19. Remove Nth Node From End of List


def remove_nth_from_end(head, n):
    slow = fast = head

    for _ in range(n):
        fast = fast.next
    if not fast:
        return head.next

    while fast.next:
        fast = fast.next
        slow = slow.next

    slow.next = slow.next.next
    return head


"""
Сначала мы используем переменную fast, которую перемещаем на n элементов вперед по списку (если fast достигает конца 
списка, то мы удаляем первый элемент). Затем в цикле while мы перемещаем как fast, так и slow до тех пор, пока fast не 
достигнет конца списка. Как только fast достигнет конца, мы выходим из цикла, и используя переменную slow, которая 
находится на n элементов позади fast, мы выполняем следующее выражение: slow.next = slow.next.next. Благодаря этому мы 
заменяем следующий элемент для переменной slow на следующий за ним элемент. В результате мы удаляем n-ый элемент списка.
"""
