class Solution:
    def is_magic_square(self, grid, r, c):
        # Check if all numbers are distinct and between 1 and 9
        values = [grid[r+i][c+j] for i in range(3) for j in range(3)]
        if sorted(values) != list(range(1, 10)):
            return False

        # Sum of rows, columns, and diagonals
        row_sums = [sum(grid[r+i][c:c+3]) for i in range(3)]
        col_sums = [sum(grid[r+i][c+j] for i in range(3)) for j in range(3)]
        diag1_sum = grid[r][c] + grid[r+1][c+1] + grid[r+2][c+2]
        diag2_sum = grid[r][c+2] + grid[r+1][c+1] + grid[r+2][c]

        all_sums = row_sums + col_sums + [diag1_sum, diag2_sum]
        
        # Check if all sums are equal to 15
        return all(x == 15 for x in all_sums)
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        if len(grid) < 3 or len(grid[0]) < 3:
            return 0

        count = 0
        for r in range(len(grid) - 2):
            for c in range(len(grid[0]) - 2):
                if self.is_magic_square(grid, r, c):
                    count += 1

        return count
            