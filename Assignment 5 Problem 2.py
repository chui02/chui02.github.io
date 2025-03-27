from collections import deque
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def minDiff(self, root: TreeNode) -> int:
        self.minimal = float('inf') #Always gets updated by first valid diff
        self.prev = None
        def inorder(node):
            if not node:
                return
            inorder(node.left)  #Visits left subtree
            if self.prev is not None: #Processes current node
                self.minimal = min(self.minimal, node.val - self.prev)
            self.prev = node.val  #Updates the previous node value
            inorder(node.right)  #Now visits right subtree
        inorder(root)
        return self.minimal

def tree(values):
    if not values or values[0] is None:
        return None
    root = TreeNode(values[0])
    queue = deque([root])
    i = 1
    
    while i < len(values):
        node = queue.popleft()
        if i < len(values) and values[i] is not None:
            node.left = TreeNode(values[i])
            queue.append(node.left)
        i += 1
        if i < len(values) and values[i] is not None:
            node.right = TreeNode(values[i])
            queue.append(node.right)
        i += 1
    return root

testCases = [
    ([4, 2, 6, 1, 3], 1),
    ([1, 0, 48, None, None, 12, 49], 1)
]

for i, (treeValue, expected) in enumerate(testCases, 1):
    root = tree(treeValue)
    solution = Solution()
    output = solution.minDiff(root)
    print(f"Example {i}: Input: {treeValue}, Output: {output}")
