class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def findHome(self, num, node):
        if num < node.val:
            if node.left:
                self.findHome(num, node.left)
            else:
                node.left = TreeNode(num)
        else:
            if node.right:
                self.findHome(num, node.right)
            else:
                node.right = TreeNode(num)

    def bstFromPreorder(self, preorder):
        root = TreeNode(preorder.pop(0))
        for num in preorder:
            self.findHome(num, root)
        return root

sol = Solution()
arr = [8, 5, 1, 7, 10, 12]
res = sol.bstFromPreorder(arr)
print(res)
