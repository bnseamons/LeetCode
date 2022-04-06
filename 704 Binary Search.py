def search(nums, target):
    l = 0
    r = len(nums)-1
    while l <=r:
        mid = (r + l) // 2
        if (nums[mid] == target):
            return mid
        elif target < nums[mid]:
            r = mid - 1
        elif target > nums[mid]:
            l = mid + 1
    lower = min(l,r)
    return lower + 1
nums = [-1,0,3,5,9,12]
target = 8
print(search(nums, target))