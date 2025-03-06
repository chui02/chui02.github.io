from collections import deque
class Tree:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class treeStuff:
    def balanceBST(self, root: Tree) -> Tree: #Inorder traversal a sorted list of elements
        values = []
        def inorder(node):
            if not node:    #Empty case
                return
            inorder(node.left)
            values.append(node.val)
            inorder(node.right)
        inorder(root)

        def balenciaga(left, right): #Making a balanced BST from given sorted elements
            if left > right:
                return None
            mid = (left + right) // 2
            rootReturn = Tree(values[mid])
            rootReturn.left = balenciaga(left, mid - 1)
            rootReturn.right = balenciaga(mid + 1, right)
            return rootReturn
        return balenciaga(0, len(values) - 1)

def BFS(root):
    if not root:    #Empty case
        return []
    result = []
    queue = deque([root])
    while queue:    #Adding left/right
        node = queue.popleft()
        if node:
            result.append(node.val)
            queue.append(node.left)
            queue.append(node.right)
        else:
            result.append(None)

    #Removing trailing elements
    while result and result[-1] is None:
        result.pop()
    return result

#Ex1: 1, null, 2, null, 3, null, 4, null, null
example1 = Tree(1)
example1.right = Tree(2)
example1.right.right = Tree(3)
example1.right.right.right = Tree(4)

sol = treeStuff()
balExample1 = sol.balanceBST(example1)
print("Example 1:", BFS(balExample1))

#Ex2: 2, 1, 3
example2 = Tree(2)
example2.left = Tree(1)
example2.right = Tree(3)

balExample2 = sol.balanceBST(example2)
print("Example 2:", BFS(balExample2))