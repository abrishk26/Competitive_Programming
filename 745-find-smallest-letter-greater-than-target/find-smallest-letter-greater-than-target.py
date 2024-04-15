class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        left = 0
        right = len(letters) - 1

        while left <= right:
            mid = (left + right) // 2

            if letters[mid] > target:
                if letters[mid - 1] <= target:
                    return letters[mid]
                else:
                    right = mid - 1
            else:
                left = mid + 1

        return letters[0]
        