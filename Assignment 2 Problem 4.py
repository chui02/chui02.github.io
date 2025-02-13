def removeDupes(s):
    stack = []       #Stack holds characters and makes it easy to just append and pop elements
    index = {ch: i for i, ch in enumerate(s)}
    tracker = set()  #Tracks current characters being used

    for i, ch in enumerate(s):  #Enumerate helps add counters to stack to loop through
        if ch not in tracker:   #If charatcer not used yet
            while stack and stack[-1] > ch and index[stack[-1]] > i:    #
                tracker.remove(stack.pop()) #Removes tracked status and pops
            stack.append(ch)    #Current character gets added and has tracked status since its now being used
            tracker.add(ch)
    return "".join(stack)   #Elements in stack are ordered alpahbetically

#Test cases from examples
s1 = "bcabc"
print(removeDupes(s1))  #Outputs "abc"
s2 = "cbacdcbc"
print(removeDupes(s2))  #Outputs "acdb"