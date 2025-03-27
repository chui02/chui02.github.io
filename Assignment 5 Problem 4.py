from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxPathSum(self, ex: Optional[TreeNode]) -> int:
        self.maxSum = float('-inf') #Global variable tracks max path sum
        def dfs(node):
            if not node:
                return 0
            leftMax = max(dfs(node.left), 0) #Max sum taken from left + right
            rightMax = max(dfs(node.right), 0)
            currentValue = node.val + leftMax + rightMax
            self.maxSum = max(self.maxSum, currentValue)
            return node.val + max(leftMax, rightMax)
        dfs(ex)
        return self.maxSum

sol = Solution()
ex1 = TreeNode(1, TreeNode(2), TreeNode(3))
print("Example 1 Output:", sol.maxPathSum(ex1))

ex2 = TreeNode(-10, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
print("Example 2 Output:", sol.maxPathSum(ex2))
