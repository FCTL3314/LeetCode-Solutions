package main

import "fmt"

func floodFill(image [][]int, sr int, sc int, color int) [][]int {
	var dfs func(int, int)

	rows := len(image) - 1
	cols := len(image[0]) - 1

	visited := make(map[[2]int]bool)
	targetColor := image[sr][sc]

	dfs = func(r int, c int) {
		if r > rows || c > cols || r < 0 || c < 0 {
			return
		}

		if image[r][c] != targetColor {
			return
		}

		if visited[[2]int{r, c}] == true {
			return
		}

		visited[[2]int{r, c}] = true

		image[r][c] = color

		dfs(r+1, c)
		dfs(r-1, c)
		dfs(r, c-1)
		dfs(r, c+1)
	}

	dfs(sr, sc)

	return image
}

func main() {
	result := floodFill(
		[][]int{{1, 1, 1}, {1, 1, 0}, {1, 0, 1}},
		1,
		1,
		2,
	)
	fmt.Println(result)
}
