# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution(object):
    def firstBadVersion(self, n):
        lo, hi = 1, n

        while lo <= hi:
            mid = (lo + hi) // 2

            if isBadVersion(mid):
                hi = mid - 1
            elif not isBadVersion(mid):
                lo = mid + 1
            
        return lo
           