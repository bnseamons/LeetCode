def twoSum(nums, target):
    numberToIndex = {}
    indicies = []
    for i in range(len(nums)):
        if (target - nums[i]) in numberToIndex.keys():
            indicies = [i, numberToIndex[target - nums[i]]]
        else:
            numberToIndex[nums[i]] = i
    return indicies


nums = [2,7,11,15]
target = 9
print(twoSum(nums, target))

