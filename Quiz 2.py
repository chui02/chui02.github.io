class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.left = left
        self.right = right
        self.val = val

#Input list 1
root1 = TreeNode(3)
root1.left = TreeNode(9)
root1.right = TreeNode(20)
root1.right.left = TreeNode(15)
root1.right.right = TreeNode(7)
#Input list 2
root2 = TreeNode(1)
root2.right = TreeNode(2) #Second in list is null so this goes right

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        left_depth = self.maxDepth(root.left)
        right_depth = self.maxDepth(root.right)
        return max(left_depth, right_depth) + 1

solOutput = Solution()

example1 = solOutput.maxDepth(root1)
print("Input: root = [3, 9, 20, null, null, 15, 7]\n Output:", example1)

example2 = solOutput.maxDepth(root2)
print("Input: root = [1, null, 2]\n Output:", example2)