# Problem: 876. Middle of the Linked List

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def middle_node(head):
    slow = fast = head
    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next
    return slow


linked_list = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5, None)))))

answer = middle_node(linked_list)
print(answer.val)

"""
Мы имеем две переменные, которые ссылаются на один и тот же стартовый элемент. Первая переменная - быстрая, она за 1 
итерацию проходит 2 элемента, а вторая переменная - медленная, за одну итерацию проходит 1 элемент. Как только быстрая 
переменная дойдёт до конца, это значит, что медленная находится ровно на середине, тут мы ее и возвращаем.
"""
