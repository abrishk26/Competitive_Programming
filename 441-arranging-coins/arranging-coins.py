class Solution:
    def arrangeCoins(self, n: int) -> int:
        left = 1
        right = n

        while left <= right:
            mid = (left + right) // 2
            sumUpToMid = ((mid * mid) + mid) // 2

            if sumUpToMid > n:
                if sumUpToMid - mid < n:
                    return mid - 1
                elif sumUpToMid - mid == n:
                    return mid - 1
                else:
                    right = mid - 1
            elif sumUpToMid < n:
                if sumUpToMid + mid + 1 > n:
                    return mid
                elif sumUpToMid + mid + 1 == n:
                    return mid + 1
                else:
                    left = mid + 1
            else:
                return mid
                

            
        