# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def __init__(self):
        self.arr = None

    def dfs(self, node, i):
        if len(self.arr) - 1 == i:
            if not node.left and not node.right:
                return True
        else:
            if node.left and node.left.val == self.arr[i + 1]:
                if self.dfs(node.left, i + 1):
                    return True
            if node.right and node.right.val == self.arr[i + 1]:
                if self.dfs(node.right, i + 1):
                    return True
        return False

    def isValidSequence(self, root: TreeNode, arr: List[int]) -> bool:
        if len(arr) < 1:
            return False
        if root.val != arr[0]:
            return False
        self.arr = arr
        return self.dfs(root, 0)
