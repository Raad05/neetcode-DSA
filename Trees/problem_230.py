# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# recursive approach
class Solution(object):
    def kthSmallest(self, root, k):
        res = []

        def inOrder(root):
            if not root:
                return

            inOrder(root.left)
            res.append(root.val)
            inOrder(root.right)

        inOrder(root)

        return res[k - 1]

# iterative approach   
class Solution(object):
    def kthSmallest(self, root, k):
        count = 0
        stack = []
        current = root

        while current or stack:
            while current:
                stack.append(current)
                current = current.left

            current = stack.pop()
            count += 1

            if count == k:
                return current.val
            
            current = current.right