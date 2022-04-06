def findDisappearedNumbers(nums):
    i = 0
    temp = 0
    numbersmislocated = []
    while i < len(nums):
        placewherenumberlookingatshouldbe = nums[i]-1
        if nums[placewherenumberlookingatshouldbe] != nums[i]:
            temp = nums[placewherenumberlookingatshouldbe]
            nums[placewherenumberlookingatshouldbe] = nums[i]
            nums[i] = temp
        else:
            i += 1
    for i in range(len(nums)):
        if nums[i] != i + 1:
            numbersmislocated.append(i+1)
    return numbersmislocated


nums = [1,1]
print(findDisappearedNumbers(nums))