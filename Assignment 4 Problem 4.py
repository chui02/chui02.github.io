from collections import deque

def shortArray(nums, k):
    n = len(nums)
    dq = deque()
    prefix = [0] * (n + 1)
    for i in range(n):
        prefix[i + 1] = prefix[i] + nums[i]
    minimum = float('inf')  #Infinity exists to check if minimim is positive
                            #Returns -1 if not (below), for no valid subarray
    for i in range(n + 1):
        while dq and prefix[i] - prefix[dq[0]] >= k:
            minimum = min(minimum, i - dq.popleft())
        while dq and prefix[i] <= prefix[dq[-1]]:
            dq.pop()
        dq.append(i)
    return minimum if minimum != float('inf') else -1

print(shortArray([1], 1))
print(shortArray([1,2], 4))    #Return -1 since invalid
print(shortArray([2,-1,2], 3))