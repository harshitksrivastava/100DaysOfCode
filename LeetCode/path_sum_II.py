# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def pathSum(self, root: TreeNode, targetSum):
        res = []
        path = []
        self.allPathSum(root, path, targetSum, res)
        return res

    def allPathSum(self, root, path, target, res):
        if root is None:
            return False
        path.append(root.val)
        if root.left is None and root.right is None:
            if sum(path) == target:
                res.append(path.copy())
                path.pop()
                return True
            else:
                path.pop()
                return False

        if self.allPathSum(root.left, path, target, res):
            pass
        if self.allPathSum(root.right, path, target, res):
            pass
        path.pop()


if __name__ == "__main__":
    #         10
    #       /    \
    #     28     13
    #          /    \
    #         14     15     10+13+15 also adds upto the required sum but 15 is not a leaf node(hence not our solution)
    #         / \    / \
    #       21  22  23  24
    root1 = TreeNode(10)
    root1.left = TreeNode(28)
    root1.right = TreeNode(13)

    root1.right.left = TreeNode(14)
    root1.right.right = TreeNode(15)

    root1.right.left.left = TreeNode(21)
    root1.right.left.right = TreeNode(22)
    root1.right.right.left = TreeNode(23)
    root1.right.right.right = TreeNode(24)

    sum1 = 38
    sol = Solution()
    ans = sol.pathSum(root1, sum1)
    print(ans)

# Example 1:
# Input: root = [5,4,8,11,null,13,4,7,2,null,null,5,1], targetSum = 22
# Output: [[5,4,11,2],[5,8,4,5]]
#
# Example 2:
# Input: root = [1,2,3], targetSum = 5
# Output: []
#
# Example 3:
# Input: root = [1,2], targetSum = 0
# Output: []
