class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        n = [num for num in range(1, n + 1)]
        
        startIndex = 0

        while len(n) > 1:
            indexToRemove = (startIndex + k - 1) % len(n)
            n.pop(indexToRemove)
            startIndex = indexToRemove
           
        return n[0]

        