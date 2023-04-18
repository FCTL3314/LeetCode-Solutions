# Problem: 1302. Deepest Leaves Sum

import collections


def deepest_leaves_sum(root):
    if not root:
        return 0

    res = []

    queue = collections.deque()
    queue.append(root)

    while queue:
        temp = []
        for _ in range(len(queue)):

            item = queue.popleft()

            if item.left:
                queue.append(item.left)
            if item.right:
                queue.append(item.right)
            temp.append(item.val)
        res.append(temp)
    return sum(res[-1])


"""
Этот алгоритм добавляет каждый уровень дерева в виде списка значений в список res, а затем возвращает сумму значений 
последнего добавленного уровня, то есть сумму значений самых глубоких листьев дерева.
"""
