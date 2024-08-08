class Solution:
    def maximumStrongPairXor(self, nums: List[int]) -> int:
        nums.sort()
        max_xor = 0
        n = len(nums)

        for i in range(n):
            for j in range(i, n):
                x, y = nums[i], nums[j]

                if abs(x - y) <= x:
                    current_xor = x ^ y
                    max_xor = max(max_xor, current_xor)
                else:
                    continue

        return max_xor

        