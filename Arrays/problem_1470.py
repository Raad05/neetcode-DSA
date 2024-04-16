class Solution(object):
    def shuffle(self, nums, n):
        arr = []
        for i in range(n):
            arr.append(nums[i])
            arr.append(nums[i + n])

        return arr
    
# sample input
# nums = [2, 5, 1, 3, 4, 7]
# n = 3