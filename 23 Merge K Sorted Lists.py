def mergeKLists(lists):
    if not lists:
        return None
    while len(lists) > 1:
        mergedLists = []
        for i in range(len(lists)):
            l1 = lists[i]
            if i+1 < len(lists):
                l2 = lists[i+1]
            mergedLists.append(mergeLists(l1, l2))
        lists = mergedLists
    return mergedLists[0]





def mergeLists(l1, l2):
    head = ListNode()
    current = head
    while l1 and l2:
        if l1.val < l2.val:
            current.next = l1
            l1 = l1.next
            current = current.next
        else:
            current.next = l2
            l2 = l2.next
            current = current.next
    if l1:
        current.next = l1
    elif l2:
        current.next = l2
        head = head.next