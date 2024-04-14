class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        
        if target > nums[-1]:
            return len(nums)
        elif target < nums[0]:
            return 0

        for i in nums:
            if i == target:
                return nums.index(i)

        nums.append(target)
        nums.sort()

        return nums.index(target)

        

        
