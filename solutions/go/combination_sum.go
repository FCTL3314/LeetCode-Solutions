package main

import "fmt"

func combinationSum(candidates []int, target int) [][]int {
	var ans [][]int
	var backtrack func(int, []int)

	backtrack = func(i int, combination []int) {
		sum := 0
		for _, num := range combination {
			sum += num
		}

		if sum == target {
			coppedCombination := make([]int, len(combination))
			copy(coppedCombination, combination)
			ans = append(ans, coppedCombination)
			return
		}

		if i > len(candidates)-1 || sum > target {
			return
		}

		combination = append(combination, candidates[i])

		backtrack(i, combination)
		combination = combination[:len(combination)-1]
		backtrack(i+1, combination)

		return

	}

	backtrack(0, []int{})

	return ans
}

func main() {
	result := combinationSum([]int{2, 3, 6, 7}, 7)
	fmt.Println(result)
}
