#Manages linked list
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def mergeLists(lists):
    #Collect all values from all linked lists
    nodes = []
    for l in lists:
        while l:
            nodes.append(l.val)
            l = l.next

    #If no nodes found, returns None
    if not nodes:
        return None

    #Sorts values
    nodes.sort()

    #Creates new linked list from sorted values
    dummy = ListNode()
    current = dummy
    for val in nodes:
        current.next = ListNode(val)
        current = current.next

    return dummy.next

def linkedToList(head):
    #Converts linked list to Python list
    result = []
    while head:
        result.append(head.val)
        head = head.next
    return result

def createLinkedList(lst):
    #Creates linked list from Python list
    if not lst:
        return None
    head = ListNode(lst[0])
    current = head
    for val in lst[1:]:
        current.next = ListNode(val)
        current = current.next
    return head

#Expected format example: (1 4 5) (1 3 4) (2 6)
#User input makes this easier to manage
user_input = input("Enter sorted linked lists (e.g., (1 4 5) (1 3 4) (2 6)): ")

#Splits input on the " ) " character for multiple lists
parts = user_input.split(")")
list_of_linked_lists = []
for part in parts:
    part = part.strip()  #Removes whitespace in input
    if part == "":  #Skips empty strings
        continue
    if part[0] == "(":
        part = part[1:]  # Remove the leading " ( " for formatting
    #Now "part" should be like "1 4 5"?
    if part:
        #Splits numbers by whitespace
        number_strs = part.split()
        numbers = []
        for num in number_strs:
            try:
                numbers.append(int(num))
            except:
                pass
        #Converts list of numbers into linked list
        linked_list = createLinkedList(numbers)
        list_of_linked_lists.append(linked_list)

#Merges k sorted linked lists
merged_head = mergeLists(list_of_linked_lists)
#Converts merged linked list into Python list
result = linkedToList(merged_head)

#Prints output and checks if it's empty
if not result:
    print("[ ]")
else:
    print(result)