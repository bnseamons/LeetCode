def threeSum(nums):
    triplets = []
    nums.sort()
    for i in range(len(nums)):
        if nums[i] == nums[i - 1] and i > 0:
            continue

        l = i+1
        r = len(nums)-1
        while l < r:
            sumOfThree = nums[i] + nums[l] + nums[r]
            if sumOfThree > 0:
                r-=1
            elif sumOfThree < 0:
                l+=1
            else:
                triplet = [nums[i], nums[l], nums[r]]
                triplets.append(triplet)
                l+=1
                while nums[l] == nums[l-1] and l<r:
                    l+=1

    return triplets





nums = [-1,0,1,2,-1,-4]
print(threeSum(nums))
