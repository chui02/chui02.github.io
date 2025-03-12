from collections import deque
class TreeNode:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

def avgValue(root):
    if not root: #Empty cases
        return []
    result = []  #Initialize as empty
    queue = deque([root])

    while queue:
        size = len(queue)
        sum = 0
        for _ in range(size):
            node = queue.popleft()
            sum += node.val
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        result.append(sum / size) #Calc avg for levels
    return result

root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)
#Visual of tree
#    3
#   / \
#  9   20
#     /  \
#    15   7
print(avgValue(root))  #Output should be: 3, 14.5, 11