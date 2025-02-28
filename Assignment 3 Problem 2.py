from collections import deque
class Tree:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class binaryTree:
    def buildTree(self, preorder, inorder): #For the input of preorer and inorder
        #For empty cases
        if not preorder or not inorder:
            return None
        #Sets first element in preorder as root
        rootVal = preorder[0]
        root = Tree(rootVal)
        mid = inorder.index(rootVal) #Index of rootVal inorder
        leftOrder = inorder[:mid] #Elements left of middle go in left subtree and right of middle go to left subtree
        rightOrder = inorder[mid+1:]
        leftPreorder = preorder[1:1 + len(leftOrder)] #Keeps length of subtree inorder same as preorder
        rightPreorder = preorder[1 + len(leftOrder):]
        root.left = self.buildTree(leftPreorder, leftOrder) #Left and right subtrees get elements recursively
        root.right = self.buildTree(rightPreorder, rightOrder)
        return root

def treePlacement(root): #Check if tree is empty, initializes queue and storing list, puts nodes through FIFO order (left/right)
    if not root:
        return []
    result = []
    queue = deque([root])
    while queue:
        node = queue.popleft()
        if node:
            result.append(node.val)
            queue.append(node.left)
            queue.append(node.right)
        else:
            result.append(None)
    #Removes trailing values b/c of spaces
    while result and result[-1] is None:
        result.pop()
    return result

if __name__ == "__main__":
    sol = binaryTree()
    #Example 1
    preorder1 = [3, 9, 20, 15, 7]
    inorder1 = [9, 3, 15, 20, 7]
    root1 = sol.buildTree(preorder1, inorder1)
    print("Output 1:", treePlacement(root1))

    #Example 2
    preorder2 = [-1]
    inorder2 = [-1]
    root2 = sol.buildTree(preorder2, inorder2)
    print("Output2 :", treePlacement(root2))