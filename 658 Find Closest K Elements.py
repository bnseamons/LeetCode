def findClosestElements(arr, k, x):
    l, r = 0, len(arr) - 1

    # Find index of x or the closest val to x
    val, idx = arr[0], 0
    while l <= r:
        m = (l + r) // 2

        if arr[m] < x:
            l = m + 1
        elif arr[m] > x:
            r = m - 1
        else:
            break
    if l > r and l == len(arr):
        idx = len(arr)-1
    elif r < l and r == -1:
        idx = 0
    elif l > r:
        idx = r
    elif r > l:
        idx = l


    l = r = idx
    for i in range(k - 1):
        if l == 0:
            r += 1
        elif r == len(arr) - 1 or x - arr[l - 1] <= arr[r + 1] - x:
            l -= 1
        else:
            r += 1
    return arr[l:r + 1]

arr = [1,3,4,5,6]
k = 4
x = 2
print(findClosestElements(arr, k, x))