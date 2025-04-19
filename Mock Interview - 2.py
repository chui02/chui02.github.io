class ListNode:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next

def cycle(head):
    slow = fast = head
    while fast and fast.next:
        slow = slow.next        #Moving one step
        fast = fast.next.next   #Moving two steps
        if slow == fast:
            return True
    return False

def linkedList (values, pos):
    if not values:
        return None
    nodes = [ListNode(val) for val in values]
    for i in range(len(nodes) - 1):
        nodes[i].next = nodes[i + 1]
        if pos != -1:
            nodes[-1].next = nodes[pos]
    return nodes[0]
    
example1 = linkedList([3, 2, 0, -4], 1)
print("Test Case Output:", cycle(example1))