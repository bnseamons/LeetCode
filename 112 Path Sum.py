def hasPathSum(root, targetSum):

    def dfs(node, currSum):
        if not node:
            return False

        currSum += node.val

        if not node.right and not node.left:
            return currSum == targetSum

        return (dfs(node.left, currSum) or dfs(node.right, currSum))

    return dfs(root, 0)