def sortedSquares(nums):
    firstNonNegative = len(nums)
    arrayOfSquares = []
    for r in range(len(nums)):
        if nums[r] >= 0:
            firstNonNegative = r
            break
    r = firstNonNegative
    l = firstNonNegative - 1
    while r < len(nums) and l >= 0:
        if nums[r]**2 > nums[l]**2:
            arrayOfSquares.append(nums[l]**2)
            l -= 1
        else:
            arrayOfSquares.append(nums[r]**2)
            r += 1
    while r < len(nums):
        arrayOfSquares.append(nums[r] ** 2)
        r += 1
    while l >= 0:
        arrayOfSquares.append(nums[l] ** 2)
        l -= 1
    return arrayOfSquares

nums = [-5,-3,-2,-1]
print(sortedSquares(nums))
