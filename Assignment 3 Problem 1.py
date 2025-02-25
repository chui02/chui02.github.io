class listToBinary:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class TreeNode:  # Set up node stuff
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def listConvert(head):
    #Converts linked list to array
    values = []
    while head:
        values.append(head.val)
        head = head.next

    #Binary search tree from given array, left to right
    def bstFormat(left, right):
        if left > right:
            return None
        #Rright middle element is used if a list has even elements (Mostly to fix bricking my program)
        mid = (left + right + 1) // 2
        node = TreeNode(values[mid])
        node.left = bstFormat(left, mid - 1)
        node.right = bstFormat(mid + 1, right)
        return node
    return bstFormat(0, len(values) - 1)  #Accounting for python format

#Dequeues node, changes list and handles left/right, also handles if input is empty
def bstListReturn(root):  
    if not root:
        return []
    queue, result = [root], []
    while queue:
        node = queue.pop(0)
        if node:
            result.append(node.val)
            queue.append(node.left)
            queue.append(node.right)
        else:
            result.append(None)

    #Removes trailing values for cleaner output since I have spaces in input
    while result and result[-1] is None:
        result.pop()
    return result

listInput = input("Enter a sorted list of integers separated by spaces: ")
if listInput.strip():
    values = list(map(int, listInput.split()))
    #Converts user input into a linked list
    dummy = listToBinary()
    current = dummy
    for val in values:
        current.next = listToBinary(val)
        current = current.next
    head = dummy.next
    #Converts input into binary search tree
    tree = listConvert(head)

    print("Output: ", bstListReturn(tree))
else:
    print("Output: []")  # If input is empty, i.e. example 2