def findDuplicates(nums):
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
    duplicates = []
    for i in range(len(nums)):
        if nums[i] != i+1:
            duplicates.append(nums[i])
    return duplicates


nums = [4,3,2,4,1,2,3,1]
print(findDuplicates(nums))