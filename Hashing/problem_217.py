class Solution(object):
    def containsDuplicate(self, nums):
        countMap = {}

        for i in nums:
            if i not in countMap:
                countMap[i] = 1
            else:
                return True
            
        return False
