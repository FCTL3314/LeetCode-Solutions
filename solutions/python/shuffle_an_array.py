# Problem: 384. Shuffle an Array

import random
from typing import List


class Solution:

    def __init__(self, nums: List[int]):
        self.nums = nums

    def reset(self) -> List[int]:
        return self.nums

    def shuffle(self) -> List[int]:
        nums_copy = self.nums.copy()
        random.shuffle(nums_copy)
        return nums_copy


obj = Solution([1, 2, 3, 4, 5])
param_1 = obj.shuffle()
param_2 = obj.reset()
param_3 = obj.shuffle()

answer = [param_1, param_2, param_3]
print(answer)

"""
Метод reset возвращает self.nums, поскольку он никогда не будет меняться. А метод shuffle создает копию self.nums, затем 
применяет к ней функцию shuffle из модуля random и возвращает эту копию.
"""
