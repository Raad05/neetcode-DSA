# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def rightSideView(self, root):
        res = []
        queue = deque()

        if root:
            queue.append(root)

        while queue:
            rightSide = None

            for i in range(len(queue)):
                current = queue.popleft()

                if current:
                    rightSide = current
                    queue.append(current.left)
                    queue.append(current.right)

            if rightSide:
                res.append(rightSide.val)

        return res