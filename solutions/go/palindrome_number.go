package main

import (
	"fmt"
)

func isPalindrome(s string) bool {
	left := 0
	right := len(s) - 1

	for left <= right {
		if s[left] != s[right] {
			return false
		}
		left++
		right--
	}

	return true
}

func main() {
	for {
		fmt.Printf("Input word: ")

		var word string
		_, err := fmt.Scan(&word)
		if err != nil {
			fmt.Printf("Error, returning...")
			return
		}

		result := isPalindrome(word)

		var humanizedResult string
		if result {
			humanizedResult = "palindrome"
		} else {
			humanizedResult = "not palindrome"
		}
		fmt.Printf("Word \"%s\" is %v\n", word, humanizedResult)
	}
}
