class TreeNode:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

def binaryTreePaths(root):
    paths = []

    def dfs(node, path):
        if not node:
            return
        path += str(node.val)

        if not node.left and not node.right:
            paths.append(path)

        else:
            path += '->'
            dfs(node.left, path)
            dfs(node.right, path)

    dfs(root, "")
    return paths

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.right = TreeNode(5)

print(binaryTreePaths(root))