def intervalIntersection(firstList, secondList):
    intersection = []
    i = 0
    j = 0
    while i < len(firstList) and j < len(secondList):
        firstInterval = firstList[i]
        secondInterval = secondList[j]
        if secondInterval[0] <= firstInterval[1] and secondInterval[0] >= firstInterval[0]:
            print("case1")
            firstVal = max(firstInterval[0], secondInterval[0])
            secondVal = min(firstInterval[1], secondInterval[1])
            intersection.append([firstVal, secondVal])
            if min(firstInterval[1], secondInterval[1]) == firstInterval[1]:
                i += 1
            else:
                j += 1
        elif firstInterval[0] <=  secondInterval[1] and firstInterval[0] >= secondInterval[0]:
            print("case2")
            firstVal = max(firstInterval[0], secondInterval[0])
            secondVal = min(firstInterval[1], secondInterval[1])
            intersection.append([firstVal, secondVal])
            if min(firstInterval[1], secondInterval[1]) == firstInterval[1]:
                i += 1
            else:
                j += 1
        elif firstInterval[0] <= secondInterval[0] and firstInterval[1] >= secondInterval[1]:
            print("case3")
            intersection.append(secondInterval)
            j += 1
        elif firstInterval[0] >= secondInterval[0] and firstInterval[1] <= secondInterval[1]:
            print("case4")
            intersection.append(firstInterval)
            i += 1
        else:
            if min(firstInterval[1], secondInterval[1]) == firstInterval[1]:
                print("case5")
                i += 1
            else:
                print("case6")
                j += 1
    return intersection

firstList = [[10,12],[18,19]]
secondList = [[1,6],[8,11],[13,17],[19,20]]
print(intervalIntersection(firstList, secondList))

