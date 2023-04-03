# Problem: 27. Remove Element

def remove_element(nums, val):
    counter = len(nums)
    while val in nums:
        nums.remove(val)
        counter -= 1
    for _ in range(counter):
        nums.append('_')
    return counter


answer = remove_element(nums=[3, 2, 2, 3], val=3)
print(answer)
