from collections import deque #pop and append 
class Tree:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class treeStuff:
    def largestValues(self, root: Tree):
        #If empty
        if not root:
            return []
        
        queue = deque([root])
        result = []
        #Level order BFS goes through the tree
        while queue:    
            list = len(queue)
            maximum = float('0')   #Tracks max value in current level
            for _ in range(list):
                node = queue.popleft()
                maximum = max(maximum, node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            result.append(maximum)
        return result
    
op = treeStuff()

if __name__ == "__main__":
    #Ex1 input: 1, 3, 2, 5, 3, null, 9
    example1 = Tree(1)
    example1.left = Tree(3, Tree(5), Tree(3))
    example1.right = Tree(2, None, Tree(9))
    print("Example 1 Output:", op.largestValues(example1))

    #Ex 2input: 1, 2, 3
    example2 = Tree(1, Tree(2), Tree(3))
    print("Example 2 Output:", op.largestValues(example2))