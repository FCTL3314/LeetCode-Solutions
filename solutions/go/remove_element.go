package main

import (
	"fmt"
)

func removeElement(nums []int, val int) int {
	i := 0
	for i <= len(nums)-1 {
		if nums[i] == val {
			nums = append(nums[:i], nums[i+1:]...)
		} else {
			i++
		}
	}
	return len(nums)
}

func main() {
	result := removeElement([]int{0, 1, 2, 2, 3, 0, 4, 2}, 2)
	fmt.Printf("Result: %v\n", result)
}
