class Solution:
    def maxScoreIndices(self, nums: List[int]) -> List[int]:
        
        indexs = [0]
        maxOnes = nums.count(1)
        temp = maxOnes
        maxZeroes = 0
        divisionScore = maxOnes

        for i in range(0, len(nums)):
            if nums[i] == 0:
                maxZeroes += 1
            else:
                temp -= 1
            if maxZeroes + temp > divisionScore:
                divisionScore = maxZeroes + temp
                indexs.clear()
                indexs.append(i + 1)
            elif maxZeroes + temp == divisionScore:
                indexs.append(i + 1)
            
        
        return indexs
        