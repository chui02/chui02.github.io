#Manages linked list
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def removeNode(head: ListNode, n: int) -> ListNode:
    #Finds length of current list (User input below)
    length = 0
    current = head
    while current:
        length += 1
        current = current.next
    
    #If n is equal to the length, removes head (If input is 1, makes it empty)
    if n == length:
        return head.next
    
    #Finds node before the one to be removed
    current = head
    for _ in range(length - n - 1):
        current = current.next
    
    #Removes nth node from end
    if current.next:
        current.next = current.next.next
    return head

#Prints out the results, doesn't match examples but it works
def printList(head: ListNode):
    current = head
    while current:
        print(current.val, end=", ")
        current = current.next
    print("End")

#Converts list of intergers to linked list
def createLinkedList(values):
    if not values:
        return None
    head = ListNode(values[0])
    current = head
    for value in values[1:]:
        current.next = ListNode(value)
        current = current.next
    return head

#User input for list, makes it easier for me to just put in manually
#I don't know if I'm just sleep deprived but I literally cannot find a way to make multiple test cases run like previously
inputs = input("Enter the elements of the linked list separated by a space: ")
#Indicates the last node to be removed
n = 1

#Turns input string into a list of integers
values = list(map(int, inputs.split()))
head = createLinkedList(values)

#Removes nth node from the end and prints result
newHead = removeNode(head, n)
printList(newHead)