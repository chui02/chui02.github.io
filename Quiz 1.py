class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

#Merging lists, recursion
class Solution:
    def mergeTwoLists(self, list1: ListNode, list2: ListNode) -> ListNode:
        if not list1:
            return list2
        if not list2:
            return list1

        if list1.val < list2.val:
            list1.next = self.mergeTwoLists(list1.next, list2)
            return list1
        else:
            list2.next = self.mergeTwoLists(list1, list2.next)
            return list2

#Converts list to linked list
def linkedList(values):
    if not values:
        return None
    head = ListNode(values[0])
    current = head
    for val in values[1:]:
        current.next = ListNode(val)
        current = current.next
    return head

#Test cases from example
list1 = linkedList([1, 2, 4])
list2 = linkedList([1, 3, 4])

#Prints linked list
def printLinkedList(head):
    values = []
    while head:
        values.append(head.val)
        head = head.next
    print(values)

solution = Solution()
mergedList = solution.mergeTwoLists(list1, list2)

#Prints merged list
printLinkedList(mergedList)