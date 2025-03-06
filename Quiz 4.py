def intersection(nums1, nums2):
    numsSet1 = set(nums1) #Converting lists to sets removes any dupes
    numsSet2 = set(nums2)
    return list(numsSet1 & numsSet2)

nums1 = [4,9,5]
nums2 = [9,4,9,8,4]
print(intersection(nums1, nums2))