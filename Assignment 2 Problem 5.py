from collections import deque #This lets me pop or append easily from both sides. I don't know if I'm allowed to actually import this, but this saves me a lot of work
def subarraySum(nums, k):
    store = deque()  #Stores indices of p to be in the increasing order of p[i]
    result = float('inf')   #Storing variable as infinity in the case of no subarray
                            #Gets replaced if valid subarray is found, otherwise turns into -1 for result (e.g. not found)
                            #I used infinity because if I did a regulor number like 9, I could run into the problem of having the answer output be the same and it'd brick the program
                            #So TLDR infinity makes it so it's impossible to match from any test case
    n = len(nums)
    p = [0] * (n + 1)
    for i in range(n):
        p[i + 1] = p[i] + nums[i]
    for i in range(n + 1):
        while store and p[i] - p[store[0]] >= k:    #Checks oldest indices store for if p[i] - p[store[0]] >= k, pops from the front is valid
            result = min(result, i - store[0])
            store.popleft()
        #Executes if p[i] is smaller and pops from back
        #p[i] will give a small prefix sum for checking
        while store and p[i] <= p[store[-1]]:
            store.pop()
        store.append(i)
    return result if result != float('inf') else -1

#Test cases
if __name__ == "__main__":
    print(subarraySum([1], 1))         #Outputs 1
    print(subarraySum([1,2], 4))       #Outputs -1 (Doesn't exist)
    print(subarraySum([2, -1, 2], 3))  #Outputs 3
