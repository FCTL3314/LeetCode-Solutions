package main

import (
	"fmt"
)

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

type Solution struct {
	ans int
}

func newSolution() *Solution {
	return &Solution{ans: 0}
}

func (s *Solution) treeTraversal(node *TreeNode) int {
	if node == nil {
		return s.ans
	}

	sum, childrenCount := s.getChildrenSum(node)
	if sum/childrenCount == node.Val {
		s.ans++
	}

	s.treeTraversal(node.Left)
	s.treeTraversal(node.Right)

	return s.ans
}

func (s *Solution) getChildrenSum(node *TreeNode) (int, int) {
	sum := 0
	childrenCount := 0
	queue := []*TreeNode{node}

	for len(queue) > 0 {
		item := queue[len(queue)-1]
		queue = queue[:len(queue)-1]

		sum += item.Val
		childrenCount++

		if item.Left != nil {
			queue = append(queue, item.Left)
		}
		if item.Right != nil {
			queue = append(queue, item.Right)
		}
	}

	return sum, childrenCount
}

func averageOfSubtree(root *TreeNode) int {
	solution := newSolution()
	return solution.treeTraversal(root)
}

func main() {
	tree := &TreeNode{
		Val: 4,
		Left: &TreeNode{
			Val: 8,
			Left: &TreeNode{
				Val:   0,
				Left:  nil,
				Right: nil,
			},
			Right: &TreeNode{
				Val:   1,
				Left:  nil,
				Right: nil,
			},
		},
		Right: &TreeNode{
			Val:  5,
			Left: nil,
			Right: &TreeNode{
				Val:   6,
				Left:  nil,
				Right: nil,
			},
		},
	}

	result := averageOfSubtree(tree)
	fmt.Println(result)
}
