class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hTable = {}

        for i, n in enumerate(nums):
            diff = target - n

            if diff in hTable:
                return [hTable[diff], i]
            
            hTable[n] = i
        
            


        
        