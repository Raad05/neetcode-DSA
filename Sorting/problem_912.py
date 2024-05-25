class Solution(object):
    # using merge sort
    def sortArray(self, nums):
        def merge(left, right):
            new = []
            i, j = 0, 0

            while i < len(left) and j < len(right):
                if left[i] <= right[j]:
                    new.append(left[i])
                    i += 1
                else:
                    new.append(right[j])
                    j += 1

            while i < len(left):
                new.append(left[i])
                i += 1

            while j < len(right):
                new.append(right[j])
                j += 1

            return new

        def mergeSort(arr):
            if len(arr) <= 1:
                return arr
            
            mid = len(arr) // 2

            left = arr[:mid]
            right = arr[mid:]

            left = mergeSort(left)
            right = mergeSort(right)

            return merge(left, right)

        return mergeSort(nums)
    
sort = Solution()
print(sort.sortArray([2, 6, 5, 1, 4, 3]))