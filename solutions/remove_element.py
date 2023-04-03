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

"""
Сначала объявляется переменная counter, которая равна длине списка. Затем, в цикле while мы проверяем наличие значения 
переменной val в списке. Если значение присутствует, то мы удаляем его из списка и уменьшаем переменную counter на 1. 
Когда значения переменной val больше нет в списке, мы добавляем в конец списка символ "_", "counter" раз. В конце, 
функция возвращает значение переменной counter. Список "nums" возвращать не нужно, так как он проверяется в самой 
функции.
"""