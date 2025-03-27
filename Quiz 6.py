class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        def inorder(node):
            if not node:
                return
            inorder(node.left)  #Left subtree
            #Creates new node in an increasing order
            self.current.right = TreeNode(node.val)
            self.current = self.current.right
            inorder(node.right)  #Right subtree
        #A dummy node handles the head
        dummy = TreeNode(-1)  
        self.current = dummy
        inorder(root)
        return dummy.right  #Returning right subtree of dummy as new root

def treeLevel(arr, root, i, n):
    if i < n and arr[i] is not None:
        root = TreeNode(arr[i])
        root.left = treeLevel(arr, root.left, 2 * i + 1, n)
        root.right = treeLevel(arr, root.right, 2 * i + 2, n)
    return root

arr = [5, 3, 6, 2, 4, None, 8, 1, None, None, None, 7, 9]
root = treeLevel(arr, None, 0, len(arr))

sol = Solution()
solRoot = sol.increasingBST(root)

def makeTree(node):
    if not node:
        return
    print(node.val, end=" -> ")
    makeTree(node.right)
makeTree(solRoot)