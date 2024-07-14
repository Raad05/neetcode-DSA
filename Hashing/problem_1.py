# using hashmap
class Solution(object):
    def twoSum(self, nums, target):
        countMap = {}

        for i, n in enumerate(nums):
            diff = target - n
            
            if diff in countMap:
                return [i, countMap[diff]]
            countMap[n] = i