class Solution(object):
    def subsets(self, nums):
        res = []
        subset = []

        def dfs(i):
            if i >= len(nums):
                res.append(subset.copy())
                return
            
            # for left decision
            subset.append(nums[i])
            dfs(i + 1)

            # for right decision
            subset.pop()
            dfs(i + 1)
        dfs(0)

        return res