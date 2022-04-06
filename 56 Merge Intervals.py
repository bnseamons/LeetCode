def merge(intervals):
    intervals.sort()
    mergedintervals = []
    p = 0
    mergedintervals.append(intervals[0])
    for i in (range(1, len(intervals))):
        currentinterval = intervals[i]
        previnternal = mergedintervals[p]
        if currentinterval[0] <= previnternal[1]:
            rightmax = max(currentinterval[1], previnternal[1])
            mergedintervals[p] = [previnternal[0], rightmax]
        else:
            p += 1
            mergedintervals.append(currentinterval)
    return mergedintervals



intervals = [[1, 4], [2, 3]]
print(merge(intervals))