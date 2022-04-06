def solution2(a):

    numToInstances = {}
    for i in range(len(a)):
        if a[i] in numToInstances:
            numToInstances.update({a[i] : 1 + numToInstances.get(a[i])})

        else:
            numToInstances.update({a[i] : 1})
    MasterList = []
    List1 = []
    List2 = []
    OnList1 = True
    Finished = True
    for key in numToInstances:
        if numToInstances.get(key) == 1:
            if OnList1:
                List1.append(key)
                OnList1 = False
            else:
                List2.append(key)
                OnList1 = True
        elif numToInstances.get(key) == 2:
            List1.append(key)
            List2.append(key)
        else:
            Finished = False
            break
    if Finished:
        MasterList.append(List1)
        MasterList.append(List2)
    return MasterList


def solution3(a):
    b = list(range(1, len(a)))
    for i in range(len(a)):
        rotate(a, 5)



def rotate(arr, n):
    x = arr[n - 1]

    for i in range(n - 1, 0, -1):
        arr[i] = arr[i - 1]

    arr[0] = x
    print(arr)



a = [3, 4, 5, 1, 2]
rotate(a, 5)