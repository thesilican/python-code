import math

# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.maxSum = 0

    def findMax(self, node):
        leftSum = self.findMax(node.left) if node.left else 0
        rightSum = self.findMax(node.right) if node.right else 0
        sum_ = node.val
        if leftSum > 0:
            sum_ += leftSum
        if rightSum > 0:
            sum_ += rightSum

        if sum_ > self.maxSum:
            self.maxSum = sum_
        return max(0, node.val + max(leftSum, rightSum, 0))

    def maxPathSum(self, root) -> int:
        self.maxSum = -math.inf

        self.findMax(root)
        return self.maxSum
