class Solution(object):
    def combinationSum(self, candidates, target):
        res = []

        def dfs(i, combination, total):
            if total == target:
                res.append(combination[:])
                return
            
            if i >= len(candidates) or total > target:
                return
            
            # for left decision
            combination.append(candidates[i])
            dfs(i, combination, total + candidates[i])

            # for right decision
            combination.pop()
            dfs(i + 1, combination, total)
        dfs(0, [], 0)

        return res
        