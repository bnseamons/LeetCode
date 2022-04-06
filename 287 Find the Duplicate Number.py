def findDuplicate(nums):
    i = 0
    temp = 0
    while i < len(nums):
        placewherenumberlookingatshouldbe = nums[i]-1
        if nums[placewherenumberlookingatshouldbe] != nums[i]:
            temp = nums[placewherenumberlookingatshouldbe]
            nums[placewherenumberlookingatshouldbe] = nums[i]
            nums[i] = temp
        else:
            i += 1
    return nums[len(nums)-1]


nums = [3,1,3,4,2]
print(findDuplicate(nums))