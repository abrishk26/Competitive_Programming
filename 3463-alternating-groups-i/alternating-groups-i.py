class Solution:
    def numberOfAlternatingGroups(self, colors: List[int]) -> int:
        alternating_groups = 0
        n = len(colors)

        for i in range(n):
            if colors[i] != colors[(i + 1) % n] and colors[(i + 1) % n] != colors[(i + 2) % n]:
                alternating_groups += 1

        return alternating_groups
