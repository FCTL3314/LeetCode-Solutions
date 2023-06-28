# Problem: 17. Letter Combinations of a Phone Number


def letter_combinations(digits):
    alphabet = {
        '2': ('a', 'b', 'c'),
        '3': ('d', 'e', 'f'),
        '4': ('g', 'h', 'i'),
        '5': ('j', 'k', 'l'),
        '6': ('m', 'n', 'o'),
        '7': ('p', 'q', 'r', 's'),
        '8': ('t', 'u', 'v'),
        '9': ('w', 'x', 'y', 'z'),
    }

    res = []

    def backtrack(i, cur):
        if len(cur) == len(digits):
            res.append(cur)
            return
        for char in alphabet[digits[i]]:
            backtrack(i + 1, cur + char)

    if digits:
        backtrack(0, '')
    return res


answer = letter_combinations(digits="23")
print(answer)

"""
В 2-й строке создаем словарь alphabet, который сопоставляет цифру с набором ее букв. В 13-й строке создаем пустой список 
res, в который будут добавляться все возможные комбинации букв.

Функция backtrack принимает два аргумента: i (текущий индекс) и cur (текущую комбинацию). Базовый случай функции 
выполняется, если длина cur равна длине digits. Тогда текущая комбинация cur добавляется в список комбинаций res. 
Иначе мы используем цикл for, чтобы перебрать буквы, соответствующие цифре digits[i], и для каждой буквы вызываем 
рекурсивно функцию backtrack, передавая аргументы i + 1 и cur + char, где char - это текущая буква, соответствующая 
цифре digits[i].
"""
