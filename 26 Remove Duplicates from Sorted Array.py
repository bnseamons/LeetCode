def removeDuplicates(nums):
    l = 0
    for r in range(len(nums)):
        if r == 0:
            continue
        if nums[r] != nums[l]:
            l += 1
            nums[l] = nums[r]

    return l+1

nums = [0,0,1,1,1,2,2,3,3,4]
print(removeDuplicates(nums))