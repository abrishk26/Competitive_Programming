class Solution:
    def mySqrt(self, x: int) -> int:
        left = 0
        right = x

        while left <= right:
            mid = (left + right) // 2

            if mid * mid == x:
                return mid
            elif (mid - 1) * (mid - 1) < x and mid * mid > x:
                return mid - 1
            elif mid * mid < x:
                left = mid + 1
            else:
                right = mid - 1
        