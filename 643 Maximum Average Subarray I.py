def findMaxAverage(nums, k):
    sumVals = 0
    subarray = nums[0:0 + k]
    for j in range(len(subarray)):
        sumVals = sumVals + subarray[j]
    maxAverage = sumVals/k
    for i in range(1, len(nums)):
        if i+k-1 < len(nums):
            sumVals = sumVals + nums [i+k-1] - nums [i-1]
            if sumVals/k > maxAverage:
                maxAverage = sumVals/k
    return maxAverage


nums = [5]
k = 1
print(findMaxAverage(nums, k))