# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def hasPathSum(self, root, targetSum):
        def dfs(root, sum):
            if not root:
                return False
            
            sum += root.val

            if not root.left and not root.right:
                return sum == targetSum
            
            return (dfs(root.left, sum) or dfs(root.right, sum))
        
        return dfs(root, 0)