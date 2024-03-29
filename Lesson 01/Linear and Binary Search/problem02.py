class Solution(object):
    # generic binary search
    def binary_search(self, lo, hi, condition):
        while lo <= hi:
            mid = (lo + hi) // 2
            result = condition(mid)

            if result == 'found':
                return mid
            elif result == 'left':
                hi = mid - 1
            elif result == 'right':
                lo = mid + 1

        return -1
    
    # find first position
    def first_position(self, nums, target):
        # condition to find first position
        def condition(mid):
            mid_number = nums[mid]

            if mid_number == target:
                if mid > 0 and nums[mid - 1] == target:
                    return 'left'
                else:
                    return 'found'
            elif mid_number > target:
                return 'left'
            elif mid_number < target:
                return 'right'
        return self.binary_search(0, len(nums) - 1, condition)
    
    # find last position
    def last_position(self, nums, target):
        # condition to find first position
        def condition(mid):
            mid_number = nums[mid]

            if mid_number == target:
                if mid < len(nums) - 1 and nums[mid + 1] == target:
                    return 'right'
                else:
                    return 'found'
            elif mid_number > target:
                return 'left'
            elif mid_number < target:
                return 'right'
        return self.binary_search(0, len(nums) - 1, condition)
    
    # return range
    def searchRange(self, nums, target):
        return [self.first_position(nums, target), self.last_position(nums, target)]