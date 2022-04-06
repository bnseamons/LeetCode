def canPartition(nums):
    if sum(nums) % 2 != 0:
        return False
    dp = set()
    dp.add(0)
    target = sum(nums) // 2
    for i in nums:
        dpcopy = dp.copy()
        print("i  = ", i)
        for j in dp:
            print("j  = ", j)
            dpcopy.add(j + i)
            if j + i == target:
                return True
        dp = dpcopy
    return False

nums = [1,2,3,5]
print(canPartition(nums))