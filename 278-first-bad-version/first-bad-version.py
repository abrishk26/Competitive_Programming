# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        left = 0
        right = n

        while left <= right:
            mid = (left + right) // 2

            callResult = isBadVersion(mid)

            if callResult:
                if isBadVersion(mid - 1):
                    right = mid - 1
                else:
                    return mid
            else:
                if isBadVersion(mid + 1):
                    return mid + 1
                else:
                    left = mid + 1
                
        