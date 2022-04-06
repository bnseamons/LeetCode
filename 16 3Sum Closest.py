def threeSum(nums):
    nums.sort()
    for i in range(len(nums)):
        if nums[i] == nums [i-1]:
            continue
        l = i + 1
        r = len(nums) - 1
        sum = nums[l] + nums[i] + nums[r]
        if sum > 0:
            print()
        elif sum < 0:
            print()
        else:
            print()





nums = [-1,0,1,2,-1,-4]




