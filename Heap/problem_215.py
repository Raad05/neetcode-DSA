class Solution(object):
    def findKthLargest(self, nums, k):
        k = len(nums) - k
        heapq.heapify(nums)
        res = 0

        while len(nums) - k > 0:
            res = heapq.heappop(nums)
            k -= 1

        return res