class Solution(object):
    # using merge sort
    def sortArray(self, nums):
        def merge(arr, LEFT, MID, RIGHT):
            left, right = arr[LEFT : MID + 1], arr[MID + 1 : RIGHT + 1]
            i, j, k = LEFT, 0, 0

            while j < len(left) and k < len(right):
                if left[j] <= right[k]:
                    arr[i] = left[j]
                    j += 1
                else:
                    arr[i] = right[k]
                    k += 1

                i += 1

            while j < len(left):
                arr[i] = left[j]
                j += 1
                i += 1

            while k < len(right):
                arr[i] = right[k]
                k += 1
                i += 1

        def mergeSort(arr, left, right):
            if left == right:
                return arr
        
            mid = (left + right) // 2

            mergeSort(arr, left, mid)
            mergeSort(arr, mid + 1, right)
            merge(arr, left, mid, right)

            return arr


        return mergeSort(nums, 0, len(nums) - 1)
