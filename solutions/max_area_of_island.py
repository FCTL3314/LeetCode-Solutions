# Problem: 695. Max Area of Island


def max_area_of_island(grid):
    rows, cols = len(grid), len(grid[0])
    path = set()

    def dfs(r, c):
        if r < 0 or c < 0 or r == rows or c == cols or (r, c) in path or grid[r][c] == 0:
            return 0
        path.add((r, c))
        return (1 + dfs(r + 1, c) +
                dfs(r - 1, c) +
                dfs(r, c - 1) +
                dfs(r, c + 1))

    area = 0

    for r in range(rows):
        for c in range(cols):
            area = max(area, dfs(r, c))

    return area


answer = max_area_of_island(
    grid=[[0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
          [0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0],
          [0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0]]
)
print(answer)
