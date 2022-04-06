def minSubArrayLen(target, nums):
    l = 0
    minlength = 100000
    sum = 0
    reachedTarget = False
    for r in range(len(nums)):
        sum += nums[r]
        while sum >= target:
            reachedTarget = True
            minlength = min(minlength, r - l + 1)
            sum -= nums[l]
            l += 1
    if reachedTarget ==  False:
        minlength = 0
    return minlength


target = 100
nums = [2,3,1,2,4,3]
print(minSubArrayLen(target, nums))
