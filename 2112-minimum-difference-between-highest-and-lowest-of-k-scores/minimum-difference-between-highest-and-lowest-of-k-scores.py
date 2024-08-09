class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        nums.sort()

        current_min_score = nums[k - 1] - nums[0]
        min_score = current_min_score

        for i in range(1, len(nums) - k + 1):
            current_min_score = nums[i + k - 1] - nums[i]
            
            min_score = min(min_score, current_min_score)

        return min_score
        