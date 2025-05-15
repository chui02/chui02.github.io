class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def longPath(root):
    if not root:
        return 0

    class Solution:
        def __init__(self):
            self.maxLength = 0

        def dfs(self, node, parentValue, length):
            if not node:
                return
            #Checks if the current node continues consecutive sequence
            if node.val == parentValue + 1:
                length += 1
            else:
                length = 1
            #Updates global maximum
            self.maxLength = max(self.maxLength, length)
            #Recurseive onto child values
            self.dfs(node.left, node.val, length)
            self.dfs(node.right, node.val, length)

    sol = Solution()
    sol.dfs(root, root.val - 1, 0)
    return sol.maxLength

root1 = TreeNode(1)
root1.right = TreeNode(3)
root1.right.left = TreeNode(2)
root1.right.right = TreeNode(4)         #Example 1
root1.right.right.right = TreeNode(5)   #[1,null,3,2,4,null,null,null,5]

root2 = TreeNode(2)
root2.right = TreeNode(3)
root2.right.left = TreeNode(2)          #Example 2
root2.right.left.left = TreeNode(1)     #[2,null,3,2,null,1]

print(longPath(root1))  #Outputs: 3 (3 - 4 - 5)
print(longPath(root2))  #Outputs: 2 (2 - 3)