# class Solution:
   
#     def getTotalIsles(self, grid: list[list[str]]) -> int:
#     #    write your code here
                    
#         return 0


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        rows, cols = len(grid), len(grid[0])
        num_islands = 0

        def dfs(row, col):
            # Base case: Out of bounds or water cell
            if row < 0 or col < 0 or row >= rows or col >= cols or grid[row][col] == "0":
                return

            # Mark the current cell as visited
            grid[row][col] = "0"

            # Explore adjacent cells (up, down, left, right)
            dfs(row + 1, col)
            dfs(row - 1, col)
            dfs(row, col + 1)
            dfs(row, col - 1)

        # Iterate through the grid
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == "1":
                    num_islands += 1
                    dfs(i, j)

        return num_islands

# Example usage:
grid_example = [
    ["1", "1", "0", "0", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "1", "0", "0"],
    ["0", "0", "0", "1", "1"]
]

solution = Solution()
result = solution.numIslands(grid_example)
print(f"Number of islands: {result}")
