class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        shuffled_str = [''] * len(indices)

        for i in range(len(indices)):
            shuffled_str[indices[i]] = s[i]

        return ''.join(shuffled_str)