class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        window = blocks[:k]
        min_oper = window.count('W')

        for i in range(1, len(blocks) - k + 1):
            window = blocks[i: k + i]
            min_oper = min(min_oper, window.count('W'))

        return min_oper