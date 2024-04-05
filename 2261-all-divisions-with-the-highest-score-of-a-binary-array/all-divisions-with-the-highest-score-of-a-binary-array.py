class Solution:
    def maxScoreIndices(self, nums: List[int]) -> List[int]:
        
        indexs = [0]
        maxOnes = nums.count(1)
        divisionScore = maxOnes
        maxScore = maxOnes


        for i in range(0, len(nums)):
            if nums[i] == 0:
                divisionScore += 1
            else:
                divisionScore -= 1
            if maxScore < divisionScore:
                indexs.clear()
                indexs.append(i + 1)
                maxScore = divisionScore
            elif maxScore == divisionScore:
                indexs.append(i + 1)
            
        
        return indexs
        