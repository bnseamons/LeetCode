def searchInsert(self, nums, target):
    l = 0
    r = len(nums) - 1
    while l <= r:
        mid = l + r // 2
        if (nums[mid] == target):
            return mid
        elif nums[mid] > target:
            r = mid - 1
        elif nums[mid] < target:
            l = mid + 1
    lower = min(l, r)
    return lower + 1


nums = [-1, 0, 3, 5, 9, 12]
target = 9
print(searchInsert(nums, target))
