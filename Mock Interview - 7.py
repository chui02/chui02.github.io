class ListNode:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next

def reverseList(head: ListNode) -> ListNode:
    prev = None
    current = head

    while current:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node

    return prev

def make_linked_list(values):
    if not values:
        return None
    head = ListNode(values[0])
    current = head
    for v in values[1:]:
        current.next = ListNode(v)
        current = current.next
    return head

def linked_list_to_list(head):
    result = []
    while head:
        result.append(head.val)
        head = head.next
    return result

examples = [
    [1, 2, 3, 4, 5],
    [1, 2],
    []
]

for i, ex in enumerate(examples, 1):
    head = make_linked_list(ex)
    reversed_head = reverseList(head)
    print(f"Example {i} Output:", linked_list_to_list(reversed_head))