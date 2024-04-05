class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        
        for i in range(len(nums)):
            if nums[i] == target:
                return i
            elif nums[len(nums) - i - 1] == target:
                return (len(nums) - i - 1)
        
        if target > nums[-1]:
            return len(nums)
        elif target < nums[0]:
            return 0
        

        temp = nums
        temp.append(target)
        temp = sorted(temp)

        return temp.index(target)

