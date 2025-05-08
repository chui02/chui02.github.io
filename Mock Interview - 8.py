class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def closestValue(root: TreeNode, target: float) -> int:
    closest = root.val
    while root:
        if abs(root.val - target) < abs(closest - target):
            closest = root.val
        if target < root.val:
            root = root.left
        else:
            root = root.right
    return closest

root = TreeNode(4)
root.left = TreeNode(2, TreeNode(1), TreeNode(3))
root.right = TreeNode(5)

target = 3.714286
print(closestValue(root, target))