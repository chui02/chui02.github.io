import math #Importing this for max
class Tree:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class treeStuff:
    def treeMaxPathSum(self, root: Tree) -> int:
        #Set to negative infinity b/c it's technically smaller than any real number w/ Python, so
        #the first comparison done will replace it including negative numbers from ex2
        #Temp workaround for negative numbers giving me compile issues
        self.maximumSum = float('-inf')
        def elemAdd(node):
            #For if empty
            if not node:
                return 0
            leftMax = max(elemAdd(node.left), 0)
            rightMax = max(elemAdd(node.right), 0)
            addedSum = node.val + leftMax + rightMax
            self.maximumSum = max(self.maximumSum, addedSum)
            return node.val + max(leftMax, rightMax)
        elemAdd(root)
        return self.maximumSum

op = treeStuff() #Easier application to test cases

#Ex1 input: 1, 2 ,3
example1 = Tree(1, Tree(2), Tree(3))
print("Example 1 output:", op.treeMaxPathSum(example1))

#Ex2 input: -10, 9, 20, (null), (null), 15, 7
example2 = Tree(-10)
example2.left = Tree(9)
example2.right = Tree(20, Tree(15), Tree(7))
print("Example 2 output:", op.treeMaxPathSum(example2))