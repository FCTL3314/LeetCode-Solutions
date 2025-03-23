# Problem: 2265. Count Nodes Equal to Average of Subtree

import collections
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def __init__(self):
        self.ans = 0

    def average_of_subtree(self, root: Optional[TreeNode]) -> int:
        self.tree_traversal(root)
        return self.ans

    def tree_traversal(self, node):
        if node is None:
            return

        subtree_sum, subtree_children = self.get_children_sum(node)
        if (subtree_sum // subtree_children) == node.val:
            self.ans += 1

        self.tree_traversal(node.left)
        self.tree_traversal(node.right)

    @staticmethod
    def get_children_sum(node):
        children_sum = 0
        children = 0

        queue = collections.deque()
        queue.append(node)

        while queue:
            item = queue.popleft()

            children_sum += item.val
            children += 1

            left = item.left
            right = item.right

            if left:
                queue.append(left)
            if right:
                queue.append(right)

        return children_sum, children


"""
В методе tree_traversal мы проходим по каждому узлу и используем метод get_children_sum, чтобы получить сумму и 
количество дочерних узлов. В строке 29 мы проверяем, равно ли среднее значение суммы дочерних узлов значению 
родительского узла. Если это так, то мы добавляем 1 к счетчику результата(self.ans). После прохода по всем узлам, 
возвращаем self.ans.
"""
