# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# with recursion
class Solution(object):
    def searchBST(self, root, val):
        if not root:
            return None
        
        if val > root.val:
            return self.searchBST(root.right, val)
        elif val < root.val:
            return self.searchBST(root.left, val)
        else:
            return root

# without recursion     
class Solution(object):
    def searchBST(self, root, val):
        current = root

        while current:
            if val > current.val:
                current = current.right
            elif val < current.val:
                current = current.left
            else:
                return current
            
        return current