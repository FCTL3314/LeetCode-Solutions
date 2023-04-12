# Problem: 79. Word Search

def exist(board, word):
    rows, cols = len(board), len(board[0])
    path = set()

    def dfs(r, c, i=0):
        if i == len(word):
            return True
        if r < 0 or c < 0 or r >= rows or c >= cols or word[i] != board[r][c] or (r, c) in path:
            return False
        path.add((r, c))
        res = (dfs(r + 1, c, i + 1) or dfs(r - 1, c, i + 1) or dfs(r, c + 1, i + 1) or dfs(r, c - 1, i + 1))
        path.remove((r, c))
        return res

    for row in range(rows):
        for column in range(cols):
            if dfs(row, column):
                return True
    return False


answer = exist(board=[["A", "B", "C", "E"],
                      ["S", "F", "C", "S"],
                      ["A", "D", "E", "E"]],
               word="ABCCED")
print(answer)

"""
Алгоритм использует поиск в глубину (DFS) для обхода всех возможных путей, начиная с каждой ячейки буквенной сетки. 
Каждая ячейка проверяется на соответствие очередной букве слова, и если это так, то происходит рекурсивный вызов функции 
dfs для продолжения поиска на соседних ячейках, до тех пор, пока не будет найдено слово целиком или пока не будут 
исчерпаны все возможные пути.

Если текущая ячейка не соответствует очередной букве слова или если уже была посещена в ходе обхода, то поиск 
прекращается и возвращается значение False.

Если слово найдено, то возвращается значение True. Если все ячейки буквенной сетки были проверены, но слово так и не 
было найдено, то возвращается значение False.
"""
