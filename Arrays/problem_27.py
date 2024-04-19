class Solution:
    def removeElement(self, nums, val):
        count = 0
        for i in range(len(nums)):
            # if element matches with val, ignore it and move to next iteration
            if nums[i] == val:
                continue
            # else, do in-place operation within the list and increase the number of count 
            nums[count] = nums[i]
            count += 1
            
        return count