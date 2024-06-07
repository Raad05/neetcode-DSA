# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def levelOrder(self, root):
        res = []
        queue = deque()

        if root:
            queue.append(root)

        while len(queue) > 0:
            levelElements = []
            for i in range(len(queue)):
                current = queue.popleft()
                levelElements.append(current.val)
                
                if current.left:
                    queue.append(current.left)

                if current.right:
                    queue.append(current.right)

            res.append(levelElements)
        
        return res