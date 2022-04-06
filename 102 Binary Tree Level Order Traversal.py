import collections


def levelOrder(root):
    result = []
    q = collections.deque
    q.append(root)

    while q != None:
        level = []
        levelSize = len(q)
        for i in range(levelSize):
            currentnode = q.popleft()
            level.append(currentnode.val)
            q.append(q.left)
            q.append(q.right)
        if level != None:
            result.append(level)
    return result
