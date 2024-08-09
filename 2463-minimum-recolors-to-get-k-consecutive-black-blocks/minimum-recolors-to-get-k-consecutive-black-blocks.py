class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        current_white_count = blocks[:k].count('W')
        min_white_count = current_white_count

        for i in range(1, len(blocks) - k + 1):
            if blocks[i - 1] == 'W':
                current_white_count -= 1

            if blocks[i + k - 1] == 'W':
                current_white_count += 1

            min_white_count = min(min_white_count, current_white_count)

        return min_white_count