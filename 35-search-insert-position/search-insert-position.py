class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        
        for i in nums:
            if i == target:
                return nums.index(i)
        
        if target > nums[-1]:
            return len(nums)
        elif target < nums[0]:
            return 0
        
        
        nums.append(target)
        nums = sorted(nums)

        return nums.index(target)
