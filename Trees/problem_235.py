# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# without recursion
class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        current = root

        while current:
            if current.val > p.val and current.val > q.val:
                current = current.left
            elif current.val < p.val and current.val < q.val:
                current = current.right
            else:
                return current
            
# with recursion
class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        if root.val > p.val and root.val > q.val:
            return self.lowestCommonAncestor(root.left, p, q)
        elif root.val < p.val and root.val < q.val:
            return self.lowestCommonAncestor(root.right, p, q)
        else:
            return root
  