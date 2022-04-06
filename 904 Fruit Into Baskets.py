def totalFruit(fruits):
    l = 0
    fruitMap = {}
    windowmax = 0
    for r in range(len(fruits)):
        rFruit = fruits[r]
        print('rFruit', rFruit)
        if rFruit in fruitMap:
            fruitMap.update({rFruit : (fruitMap.get(rFruit))+1})
        else:
            fruitMap.update({rFruit : 1})
        while len(fruitMap) > 2:
            lFruit = fruits[l]
            fruitMap.update({lFruit: (fruitMap.get(lFruit)) - 1})
            if fruitMap.get(lFruit) == 0:
                fruitMap.pop(lFruit)
            l += 1
        print(fruitMap)
        windowmax = max(windowmax, r-l+1)
    return windowmax






fruits = [1,0,1,4,1,4,1,2,3]
print(totalFruit(fruits))