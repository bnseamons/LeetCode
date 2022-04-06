def maxSubArray(nums):
    globalmax = -100000
    currentmax = -100000
    for i in range(len(nums)):
        if nums[i] > currentmax:
            currentmax = nums[i]
        else:
            currentmax = currentmax + nums[i]
        if currentmax > globalmax:
            globalmax = currentmax
    return globalmax




nums = [-2,1,-3,4,-1,2,1,-5,4]
print(maxSubArray(nums))




