# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# using recursion
class Solution(object):
    def insertIntoBST(self, root, val):
        if not root:
            return TreeNode(val)
        
        if val > root.val:
            root.right = self.insertIntoBST(root.right, val)
        elif val < root.val:
            root.left = self.insertIntoBST(root.left, val)
            
        return root
    
# without recursion
class Solution(object):
    def insertIntoBST(self, root, val):
        if not root:
            return TreeNode(val)
        
        current = root

        while True:
            if val > current.val:
                if current.right:
                    current = current.right
                else:
                    current.right = TreeNode(val)
                    break
            elif val < current.val:
                if current.left:
                    current = current.left
                else:
                    current.left = TreeNode(val)
                    break

        return root