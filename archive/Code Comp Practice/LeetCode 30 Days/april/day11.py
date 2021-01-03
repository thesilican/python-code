from typing import Tuple
# Definition for a binary tree node.


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def getScore(self, node: TreeNode) -> Tuple[int, int]:
        # Calculate left and right scores
        depthL = 0
        depthR = 0
        maxScoreL = 0
        maxScoreR = 0
        if node.left == None:
            depthL = 0
        else:
            l = self.getScore(node.left)
            depthL = l[0]
            maxScoreL = l[1]
        if node.right == None:
            depthR = 0
        else:
            r = self.getScore(node.right)
            depthR = r[0]
            maxScoreR = r[1]
        myScore = depthL + depthR + 1

        return (max(depthL, depthR) + 1, max(myScore, maxScoreL, maxScoreR))

    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        if root == None:
            return 0
        return self.getScore(root)[1] - 1


# Build a tree
if __name__ == "__main__":
    sol = Solution()
    print(sol.diameterOfBinaryTree(None))
    t1 = TreeNode(1)
    t2 = TreeNode(2)
    t3 = TreeNode(3)
    t4 = TreeNode(4)
    t5 = TreeNode(5)
    t1.left = t2
    t1.right = t3
    t2.left = t4
    t2.right = t5
    print(sol.diameterOfBinaryTree(t1))

    