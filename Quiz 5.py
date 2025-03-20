class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        if not root:
            return 0
        left_sum = 0
        if root.left and not root.left.left and not root.left.right:
            left_sum += root.left.val
        return left_sum + self.sumOfLeftLeaves(root.left) + self.sumOfLeftLeaves(root.right) #Recursively goes through the left and right subtrees

#Example 1 input: 3, 9, 20, null, null, 15, 7
root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)
sol = Solution()
print(sol.sumOfLeftLeaves(root))

#Example 2 input of just 1
root2 = TreeNode(1)
sol = Solution()
print(sol.sumOfLeftLeaves(root2))