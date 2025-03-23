# Problem: 39. Combination Sum


def combination_sum(candidates, target):
    ans = []

    def backtrack(i, combination):
        total = sum(combination)
        if total == target:
            ans.append(combination.copy())
            return
        if i >= len(candidates) or total > target:
            return

        combination.append(candidates[i])
        backtrack(i, combination)
        combination.pop()
        backtrack(i + 1, combination)

    backtrack(0, list())

    return ans


answer = combination_sum(candidates=[2, 3, 6, 7], target=7)
print(answer)

"""
В строке 5 создается пустой список ans, который будет хранить все валидные комбинации. Функция dfs принимает два 
аргумента: i - текущий индекс и combination - текущую комбинацию. Внутри функции есть 2 базовых случая: если текущая 
комбинация равна целевой сумме target, то она добавляется в список ans, а если сумма текущей комбинации больше целевой 
суммы target, то функция завершается. Если базовые случаи не выполнились, то к текущей комбинации добавляется новый 
элемент candidates[i], и функция dfs вызывается снова, но уже с i + 1 и измененной комбинацией. Затем последний 
добавленный элемент удаляется из комбинации, и функция dfs вызывается снова, но уже с i + 1 и изначальной комбинацией. 
Таким образом, функция рекурсивно перебирает все возможные комбинации. В конце функция возвращает список всех валидных 
комбинаций.
"""
