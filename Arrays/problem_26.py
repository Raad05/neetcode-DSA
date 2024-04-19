class Solution:
    def removeDuplicates(self, nums):
        count = 0
        for i in range(len(nums)):
            # if elements match, ignore it and move to next iteration
            if i < len(nums) - 1 and nums[i] == nums[i + 1]:
                continue
            # else, it gets clear that the element is unique or it is the last duplicate element in the list
            # do in-place operation within the list and increase the number of count 
            nums[count] = nums[i]
            count += 1

        return count